# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.


from collections import deque
from math import sqrt


# time complexity: O(n * sqrt(n)) - we check all numbers from 2 to sqrt(n) for each number
def min_steps_to_one(n: int) -> int:
    visited = set()
    # (curr_number, steps) - breadth-first search
    queue: deque[tuple[int, int]] = deque(
        [(n, 0)])  # each operation takes O(1) time

    while queue:
        current, steps = queue.popleft()

        if current == 1:
            return steps  # found the shortest path

        if current not in visited:
            visited.add(current)

            # add the next numbers to the queue
            queue.append((current - 1, steps + 1))

            # add next steps by finding divisors and decrementing n to the larger of a and b
            for i in range(2, int(sqrt(current)) + 1):
                if current % i == 0:
                    queue.append((max(i, current // i), steps + 1))

    return -1  # no path found


# Output should be 5, as per the example (100 -> 10 -> 9 -> 3 -> 2 -> 1)
print(min_steps_to_one(100))
