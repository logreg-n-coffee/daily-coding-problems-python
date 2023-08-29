# You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

# Dominoes, or 2 x 1 rectangles.
# Trominoes, or L-shapes.
# For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

# A B B C
# A B C C
# Given an integer N, determine in how many ways this task is possible.

# Solution: f(n) = f(n-1) + f(n-2) + 2*g(n-2) - O(N) time and O(N) space
def tilings(n):
    f = [0] * (n + 1)
    g = [0] * (n + 1)

    f[1] = 1
    f[2] = 2
    g[1] = 1
    g[2] = 2

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2] + 2 * g[i - 2]
        g[i] = g[i - 1] + f[i - 1]

    return f[n]
