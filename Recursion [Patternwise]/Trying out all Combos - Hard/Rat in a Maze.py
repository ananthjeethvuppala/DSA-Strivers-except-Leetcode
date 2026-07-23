# Rat in a Maze

# Problem Statement: Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1). Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).
# The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.

def findPath(grid, n):

    ans = []

    if grid[0][0] == 0:
        return ans

    visited = []
    for i in range(n):
        visited.append([False] * n)

    def solve(row, col, path):

        if row == n - 1 and col == n - 1:
            ans.append(path)
            return

        visited[row][col] = True

        if (
            row + 1 < n and
            grid[row + 1][col] == 1 and
            visited[row + 1][col] == False
        ):
            solve(row + 1, col, path + 'D')

        if (
            col - 1 >= 0 and
            grid[row][col - 1] == 1 and
            visited[row][col - 1] == False
        ):
            solve(row, col - 1, path + 'L')

        if (
            col + 1 < n and
            grid[row][col + 1] == 1 and
            visited[row][col + 1] == False
        ):
            solve(row, col + 1, path + 'R')

        if (
            row - 1 >= n and
            grid[row - 1][col] == 1 and
            visited[row - 1][col] == False
        ):
            solve(row - 1, col, path + 'U')

        visited[row][col] = False

    solve(0, 0, "")

    return ans

# Driver Code
n = 4

grid = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

print(findPath(grid, n))
        