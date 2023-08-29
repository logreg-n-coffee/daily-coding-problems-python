# You are the technical director of WSPT radio, serving listeners nationwide.
# For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).

# Given a list of N listeners, and a list of M radio towers,
# each placed at various locations along this line,
# determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

# For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15].
# In this case the minimum range would be 5, since that would be required for
# the tower at position 15 to reach the listener at position 20.

def find_min_range(listeners: list[int], towers: list[int]) -> int:
    listeners.sort()
    towers.sort()

    min_range = 0  # To store the minimum range needed to cover all listeners

    # Loop through all listeners
    for listener in listeners:
        # Calculate the minimum distance to a tower for this listener
        # Initialize to a very large value
        closest_tower_distance = float("inf")

        for tower in towers:
            distance = abs(tower - listener)
            closest_tower_distance = min(closest_tower_distance, distance)

        # Update the minimum range needed to cover all listeners
        min_range = int(max(min_range, closest_tower_distance))

    return min_range


# Test the function with the given example
listeners = [1, 5, 11, 20]
towers = [4, 8, 15]

result = find_min_range(listeners, towers)
print("The minimum broadcast range is:", result)
