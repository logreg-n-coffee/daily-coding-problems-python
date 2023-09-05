# An 8-puzzle is a game played on a 3 x 3 board of tiles, with the ninth tile missing.
# The remaining tiles are labeled 1 through 8 but shuffled randomly.
# Tiles may slide horizontally or vertically into an empty space, but may not be removed from the board.

# Design a class to represent the board, and find a series of steps to bring the board to
# the state [[1, 2, 3], [4, 5, 6], [7, 8, None]].

import heapq
from copy import deepcopy


class Board:
    def __init__(self, nums, goal=[1, 2, 3, 4, 5, 6, 7, 8, 0]):
        self.goal = goal
        self.tiles = nums
        self.empty = self.tiles.index(0)
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def manhattan(self, a, b):
        a_row, a_col = a // 3, a % 3
        b_row, b_col = b // 3, b % 3
        return abs(a_row - b_row) + abs(a_col - b_col)

    def calculate_heuristic(self):
        total = 0
        for digit in range(1, 9):
            total += self.manhattan(self.tiles.index(digit),
                                    self.goal.index(digit))
        return total

    def swap(self, empty, diff):
        tiles = deepcopy(self.tiles)
        tiles[empty], tiles[empty + diff] = tiles[empty + diff], tiles[empty]
        return tiles

    def get_moves(self):
        successors = []
        empty = self.empty

        if empty // 3 > 0:
            successors.append((Board(self.swap(empty, -3)), 'U'))
        if empty // 3 < 2:
            successors.append((Board(self.swap(empty, +3)), 'D'))
        if empty % 3 > 0:
            successors.append((Board(self.swap(empty, -1)), 'L'))
        if empty % 3 < 2:
            successors.append((Board(self.swap(empty, +1)), 'R'))

        return successors


def search(start):
    heap = []
    closed = set()
    heapq.heappush(heap, (start.heuristic, 0, start, ''))

    while heap:
        _, moves, board, path = heapq.heappop(heap)
        if board.tiles == board.goal:
            return moves, path

        closed.add(tuple(board.tiles))
        for successor, direction in board.get_moves():
            if tuple(successor.tiles) not in closed:
                item = (successor.heuristic + moves + 1,
                        moves + 1, successor, path + direction)
                heapq.heappush(heap, item)

    return float('inf'), None


def is_solvable(nums):
    inv_count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] != 0 and nums[j] != 0 and nums[i] > nums[j]:
                inv_count += 1
    return inv_count % 2 == 0


def solve(nums):
    if not is_solvable(nums):
        return "Unsolvable puzzle"
    start = Board(nums)
    count, path = search(start)
    return count, path


case1 = [2, 8, 3, 1, 6, 4, 7, 0, 5]
print(solve(case1))

case2 = [1, 2, 3, 4, 5, 6, 0, 7, 8]
print(solve(case2))
