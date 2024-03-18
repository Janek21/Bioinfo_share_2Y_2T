from collections import deque

def is_valid_move(row, col, rows, cols, grid):
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

def find_furthest_treasure(grid, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    dp = [[-1] * cols for _ in range(rows)]  # Initialize dp table with -1 to denote unexplored cells
    queue = deque([(start_row - 1, start_col - 1)])
    dp[start_row - 1][start_col - 1] = 0  # Initial distance from the starting position is 0

    while queue:
        row, col = queue.popleft()

        if visited[row][col]:
            continue

        visited[row][col] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc
            if is_valid_move(new_row, new_col, rows, cols, grid) and not visited[new_row][new_col]:
                dp[new_row][new_col] = dp[row][col] + 1  # Update distance to the new cell
                queue.append((new_row, new_col))

    max_distance = -1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 't':
                max_distance = max(max_distance, dp[row][col])

    return max_distance if max_distance != -1 else -1

# Input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
start_row, start_col = map(int, input().split())

# Find the furthest treasure using dynamic programming
distance = find_furthest_treasure(grid, start_row, start_col)

# Output
if distance == -1:
    print("no treasure can be reached")
else:
    print("maximum distance:", distance)
