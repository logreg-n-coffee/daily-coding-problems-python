# You are given a 2-d matrix where each cell consists of either /, \, or an empty space.
# Write an algorithm that determines into how many regions the slashes divide the space.

# For example, suppose the input for a three-by-six grid is the following:

# \    /
#  \  /
#   \/
# Considering the edges of the matrix as boundaries, this divides the grid into three triangles, so you should return 3.


# 1. Create a new grid (let's call it regionsGrid) of size 3n x 3m,
# where n is the number of rows and m is the number of columns in the given matrix.

# 2. Populate this regionsGrid based on the given matrix.
# If a cell in the matrix contains a '/', then mark the corresponding diagonal in the regionsGrid.
# Similarly, for a '', mark the opposite diagonal.

# 3. After you've populated regionsGrid, treat it as a graph problem.
# Each cell in regionsGrid that isn't part of a slash is a node.
# You can then use Depth-First Search (DFS) or Breadth-First Search (BFS) to count the number of separate regions.

# 4. Iterate over each cell in regionsGrid. If it's not visited and not part of a slash,
# increment your regions count and initiate a DFS/BFS to mark all the connected cells as visited.


def count_regions(mat: list[list[str]]) -> int:
    # convert the matrix to the regions grid (more granular than the original matrix)
    n, m = len(mat), len(mat[0])
    regions_grid = [[' ' for _ in range(3 * m)] for _ in range(3 * n)]

    for i in range(n):
        for j in range(m):
            #    /
            #   /
            #  /
            if mat[i][j] == '/':
                # places the top of the slash. Since we're working with a 3x3 block, the top of the slash is on the rightmost cell of the top row.
                regions_grid[3 * i][3 * j + 2] = "/"
                # places the middle of the slash.
                regions_grid[3 * i + 1][3 * j + 1] = "/"
                # places the bottom of the slash.
                regions_grid[3 * i + 2][3 * j] = "/"
            # \
            #  \
            #   \
            elif mat[i][j] == '\\':
                # places the top of the backslash. It's on the leftmost cell of the top row.
                regions_grid[3 * i][3 * j] = "\\"
                # places the middle of the backslash.
                regions_grid[3 * i + 1][3 * j + 1] = "\\"
                # places the bottom of the backslash.
                regions_grid[3 * i + 2][3 * j + 2] = "\\"

    def dfs(x, y):
        if x < 0 or x >= 3 * n or y < 0 or y >= 3 * m or regions_grid[x][y] in ['/', '\\', 'X']:
            return

        regions_grid[x][y] = 'X'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    # count the number of regions
    count = 0
    for i in range(3 * n):
        for j in range(3 * m):
            if regions_grid[i][j] == ' ':
                count += 1
                dfs(i, j)

    for row in regions_grid:
        print(''.join(row))

    return count


if __name__ == "__main__":
    # Test
    matrix = [
        ['\\', ' ', ' ', ' ', ' ',  '/'],
        [' ', '\\', ' ', ' ', '/', ' '],
        [' ', ' ', '\\', '/', ' ', ' ']
    ]
    print(count_regions(matrix))  # Expected output: 3
