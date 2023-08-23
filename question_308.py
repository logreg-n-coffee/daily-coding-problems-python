# You are presented with an array representing a Boolean expression. The elements are of two kinds:

# T and F, representing the values True and False.
# &, |, and ^, representing the bitwise operators for AND, OR, and XOR.
# Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.

# For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).

# Intuition: The idea is to break down the expression into sub-expressions,
# compute the number of ways to group each sub-expression to get True (or False),
# and then combine these results to get the number of ways to group the entire expression to get True.

def count_ways(expr):
    n = len(expr)

    # Helper function to determine the result of applying an operator
    # to two boolean values.
    def operate(op, a, b):
        if op == '&':
            return a & b
        elif op == '|':
            return a | b
        elif op == '^':
            return a ^ b

    # dp[i][j][k] represents the number of ways to evaluate the sub-expression
    # from index i to j (inclusive) that results in the boolean value k.
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

    # Base cases: Set the appropriate index to 1 based on whether the expression
    # at that position is 'T' (True) or 'F' (False).
    for i in range(n):
        if expr[i] == 'T':
            dp[i][i][1] = 1
        elif expr[i] == 'F':
            dp[i][i][0] = 1

    # We start evaluating sub-expressions of length 3 and increase the length
    # by 2 until we reach the full length of the expression. This is because valid
    # expressions (like "T|F" or "F&T") are of odd lengths.
    for length in range(3, n + 1, 2):  # Only consider odd lengths
        # For a given length, iterate through the expression to get all possible
        # sub-expressions of that length.
        for i in range(n - length + 1):
            j = i + length - 1  # end index of the current sub-expression

            # m iterates through the operators in the current sub-expression.
            # Operators are present at even indices.
            for m in range(i + 1, j, 2):  # m is the index of an operator
                operator = expr[m]

                # Compute all possible combinations of the results of
                # the two split sub-expressions.
                for k, x, y in [(k, x, y) for k in [0, 1] for x in [0, 1] for y in [0, 1]]:
                    if operate(operator, x, y) == k:
                        dp[i][j][k] += dp[i][m - 1][x] * dp[m + 1][j][y]

    return dp[0][n - 1][1]


expr = ['F', '|', 'T', '&', 'T']
print(count_ways(expr))  # Expected: 2
