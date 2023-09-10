# Consider the following scenario: there are N mice and N holes placed at integer points along a line.
# Given this, find a method that maps mice to holes such that the largest number of steps any mouse
# takes is minimized.

# Each move consists of moving one mouse one unit to the left or right,
# and only one mouse can fit inside each hole.

# For example, suppose the mice are positioned at [1, 4, 9, 15],
# and the holes are located at [10, -5, 0, 16]. In this case,
# the best pairing would require us to send the mouse at 1 to the hole at -5,
# so our function should return 6.


## The time complexity of this solution is O(N log N) because of the sorting step.
## The space complexity is O(1) because we are not using any extra space.
def send(mice, holes):
    mice.sort()
    holes.sort()

    moves = 0
    for i in range(len(mice)):
        moves = max(moves, abs(mice[i] - holes[i]))

    return moves


if __name__ == "__main__":
    print(send([1, 4, 9, 15], [10, -5, 0, 16]))
