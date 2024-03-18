from collections import deque

def is_valid_move(row, col, rows, cols, grid):
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

def count_accessible_treasures(grid, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_row - 1, start_col - 1)])

    accessible_treasures = 0

    while queue:
        row, col = queue.popleft()

        if grid[row][col] == 't' and not visited[row][col]:
            accessible_treasures += 1

        if visited[row][col]:
            continue

        visited[row][col] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc
            if is_valid_move(new_row, new_col, rows, cols, grid):
                queue.append((new_row, new_col))

    return accessible_treasures

# Input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
start_row, start_col = map(int, input().split())

# Count accessible treasures
accessible_treasures = count_accessible_treasures(grid, start_row, start_col)

# Output
print(accessible_treasures)
