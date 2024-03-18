from collections import deque

def is_valid_move(row, col, rows, cols, grid):
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

def find_nearest_treasure(grid, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    dp = [[float('inf')] * cols for _ in range(rows)]  # Initialize dp table with infinite distances
    queue = deque([(start_row - 1, start_col - 1)])

    dp[start_row - 1][start_col - 1] = 0  # Distance from starting position to itself is 0

    while queue:
        row, col = queue.popleft()

        if grid[row][col] == 't':
            return dp[row][col]  # Return the minimum distance to the nearest treasure

        if visited[row][col]:
            continue

        visited[row][col] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc
            if is_valid_move(new_row, new_col, rows, cols, grid):
                if dp[row][col] + 1 < dp[new_row][new_col]:
                    dp[new_row][new_col] = dp[row][col] + 1
                    queue.append((new_row, new_col))

    return -1  # If no treasure is reachable

# Input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
start_row, start_col = map(int, input().split())

# Find the nearest treasure using dynamic programming
distance = find_nearest_treasure(grid, start_row, start_col)

# Output
if distance == -1:
    print("no treasure can be reached")
else:
    print("minimum distance:", distance)
