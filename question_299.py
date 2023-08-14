# A group of houses is connected to the main water plant by means of a set of pipes.
# A house can either be connected by a set of pipes extending directly to the plant,
# or indirectly by a pipe to a nearby house which is otherwise connected.

# For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:

# A <--> B <--> C <--> plant
# Each pipe has an associated cost, which the utility company would like to minimize.
# Given an undirected graph of pipe connections, return the lowest cost configuration
# of pipes such that each house has access to water.

# In the following setup, for example, we can remove all but the pipes from
# plant to A, plant to B, and B to C, for a total cost of 16.

# pipes = {
#     'plant': {'A': 1, 'B': 5, 'C': 20},
#     'A': {'C': 15},
#     'B': {'C': 10},
#     'C': {}
# }

# Intuition: use Kruskal's algorithm to find the minimum spanning tree (MST).
# The idea is to sort all the edges in increasing order of their weights,
# and then pick the smallest edge one by one, ensuring that adding the edge to the MST doesn't form a cycle.

# Step by Step:
# 0. Convert the dict into a list of edges with their weights
# 1. Sort all the edges in non-decreasing order of their weight
# 2. Create a union-find (or disjoint-set) data structure to keep track of which vertices are in which set.
# 3. Iterate over the sorted edges and add them to the MST if adding the edge doesn't form a cycle.


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        # If ranks are same, then make one as root and increment its rank by one
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(pipes):
    edges: list[tuple[int, str, str]] = []
    for u, neighbors in pipes.items():
        for v, weight in neighbors.items():
            edges.append((weight, u, v))

    # Sort all the edges in non-decreasing order of their weight
    edges.sort()

    result: list[tuple[str, str, int]] = []
    parent: dict[str, str] = {}
    rank = {}

    # create V subsets with single elements
    for node in pipes:
        parent[node] = node
        rank[node] = 0

    index = 0  # Index variable, used for sorted edges
    e = 0  # Number of edges to be taken into account

    while e < len(pipes) - 1:
        weight, u, v = edges[index]
        index += 1

        x = find(parent, u)
        y = find(parent, v)

        # If including this edge doesn't cause cycle, include it in result
        if x != y:
            e += 1
            result.append((u, v, weight))
            union(parent, rank, x, y)

    print('parent', parent)
    print('rank', rank)

    return result


# Given pipes dictionary
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}

# Calculate the minimum cost configuration
min_cost_config = kruskal(pipes)
lowest_cost = sum(min_cost_config[i][2] for i in range(len(min_cost_config)))
print(min_cost_config)
print('lowest cost:', lowest_cost)
