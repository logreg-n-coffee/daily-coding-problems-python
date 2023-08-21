# A knight is placed on a given square on an 8 x 8 chessboard. It is then moved randomly several times,
# where each move is a standard knight move. If the knight jumps off the board at any point, however,
# it is not allowed to jump back on.

# After k moves, what is the probability that the knight remains on the board?

def get_moves(x, y):
    moves = [(1, 2), (2, 1), (2, -1), (1, -2),
             (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    return [(x + i, y + j) for (i, j) in moves]


def on_board(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7


def get_probability(x, y, k, memo={}):
    if (x, y, k) in memo:
        return memo[(x, y, k)]

    if k == 0:
        return on_board(x, y)

    if not on_board(x, y):
        return 0

    jumps = get_moves(x, y)
    probs = [get_probability(x, y, k - 1, memo) for x, y in jumps]

    memo[(x, y, k)] = 1/8 * sum(probs)

    return memo[(x, y, k)]


# Test Cases
if __name__ == "__main__":
    test_cases = [
        (4, 4, 2),    # Center of the board
        (0, 0, 2),    # Top-left corner
        (0, 3, 3),    # Edge but not a corner
        (4, 4, 0),    # k is 0
        (4, 4, 10)    # Large k to test efficiency
    ]

    for x, y, k in test_cases:
        print(
            f"Starting from ({x}, {y}) with {k} moves, probability: {get_probability(x, y, k):.5f}")
