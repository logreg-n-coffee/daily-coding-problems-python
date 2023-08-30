# In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.
#
# Here is an example:
#
# 1 2 3 4 8
# 5 1 2 3 4
# 4 5 1 2 3
# 7 4 5 1 2
#
# Write a program to determine whether a given input is a Toeplitz matrix.

def is_toeplitz(mat: list[list[int]]) -> bool:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i > 0 and j > 0 and mat[i][j] != mat[i - 1][j - 1]:
                return False
    return True


# Example usage
matrix1 = [
    [1, 2, 3, 4, 8],
    [5, 1, 2, 3, 4],
    [4, 5, 1, 2, 3],
    [7, 4, 5, 1, 2]
]

matrix2 = [
    [1, 2, 3],
    [5, 1, 2],
    [6, 5, 1]
]

print(is_toeplitz(matrix1))  # Output should be True
print(is_toeplitz(matrix2))  # Output should be True
