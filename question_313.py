# You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order.
# Each of these wheels rotate clockwise and counterclockwise.

# In addition, the lock has a certain number of "dead ends",
# meaning that if you turn the wheels to one of these combinations,
# the lock becomes stuck in that state and cannot be opened.

# Let us consider a "move" to be a rotation of a single wheel by one digit,
# in either direction. Given a lock initially set to 000, a target combination,
# and a list of dead ends,
# write a function that returns the minimum number of moves required to
# reach the target state, or None if this is impossible.

from collections import deque


def open_lock(target, deadends):
    # Convert deadends to a set for O(1) lookups
    deadends = set(deadends)

    # Check for immediate failure cases
    if "000" in deadends or target in deadends:
        return None
    if target == "000":
        return 0

    # Initialize the queue and visited set for BFS
    queue: deque[tuple[str, int]] = deque([("000", 0)])
    visited = set(["000"])

    while queue:
        # Dequeue the next state and move count
        state, moves = queue.popleft()

        # Generate all possible next states
        for i in range(3):
            for d in [-1, 1]:
                # Calculate the next digit for this wheel
                next_digit = (int(state[i]) + d) % 10

                # Generate the next state string
                next_state = state[:i] + str(next_digit) + state[i+1:]

                # If we've found the target, return the moves
                if next_state == target:
                    return moves + 1

                # If this is a deadend or visited state, skip it
                if next_state in deadends or next_state in visited:
                    continue

                # Mark this state as visited and enqueue it
                visited.add(next_state)
                queue.append((next_state, moves + 1))

    return None


# Test the function
target = "123"
deadends = ["010", "001", "111", "100"]
result = open_lock(target, deadends)
print(f"Minimum number of moves to open the lock: {result}")
