# A competitive runner would like to create a route that starts and ends at his house,
# with the condition that the route goes entirely uphill at first, and then entirely downhill.

# Given a dictionary of places of the form {location: elevation},
# and a dictionary mapping paths between some of these locations to their corresponding distances,
# find the length of the shortest route satisfying the condition above.
#
# Assume the runner's home is location 0.
#
# For example, suppose you are given the following input:
#
# elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
# paths = {
#     (0, 1): 10,
#     (0, 2): 8,
#     (0, 3): 15,
#     (1, 3): 12,
#     (2, 4): 10,
#     (3, 4): 5,
#     (3, 0): 17,
#     (4, 0): 10
# }
# In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.

# Since we must go uphill before going downhill, there must be some point p on our route with maximum elevation.
# Therefore, we can solve this problem by finding the shortest route from 0 to p, and from p back to 0, for all possible choices of p.

from collections import defaultdict
from typing import Dict, List, Tuple, DefaultDict, Any


def helper(v: int, visited: List[bool], stack: List[int], edges: DefaultDict[int, List[Tuple[int, int]]]) -> None:
    visited[v] = True

    for neighbor, _ in edges[v]:
        if not visited[neighbor]:
            helper(neighbor, visited, stack, edges)

    stack.append(v)


def toposort(edges: DefaultDict[int, List[Tuple[int, int]]], num_vertices: int) -> List[int]:
    visited: List[bool] = [False for _ in range(num_vertices)]
    stack: List[int] = []

    for v in range(num_vertices):
        if not visited[v]:
            helper(v, visited, stack, edges)

    return stack


def get_distances(edges: DefaultDict[int, List[Tuple[int, int]]], stack: List[int]) -> List[float]:
    dist: List[float] = [float('inf') for _ in range(len(stack))]
    dist[0] = 0

    while stack:
        curr = stack.pop()

        for neighbor, distance in edges[curr]:
            if dist[neighbor] > dist[curr] + distance:
                dist[neighbor] = dist[curr] + distance

    return dist[1:]


def shortest_route(elevations: Dict[int, int], paths: Dict[Tuple[Any, Any], int]) -> float:
    uphill_edges: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
    downhill_edges: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
    all_edges: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

    for (start, end), distance in paths.items():
        all_edges[start].append((end, distance))
        if elevations[start] < elevations[end]:
            uphill_edges[start].append((end, distance))
        else:
            downhill_edges[end].append((start, distance))

    num_vertices: int = len(all_edges.keys())
    stack: List[int] = toposort(all_edges, num_vertices)

    uphill_distances: List[float] = get_distances(uphill_edges, list(stack))
    downhill_distances: List[float] = get_distances(
        downhill_edges, list(stack))

    return min(x + y for x, y in zip(uphill_distances, downhill_distances))


if __name__ == '__main__':
    elevations: Dict[int, int] = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
    paths: Dict[Tuple[int, int], int] = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 17,
        (4, 0): 10
    }
    print(shortest_route(elevations, paths))
