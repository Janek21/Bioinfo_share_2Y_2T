from collections import deque

def is_valid_move(row, col, rows, cols, grid):
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

def find_second_furthest_treasure(grid, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_row - 1, start_col - 1, 0)])
    distances = []

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == 't' and not visited[row][col]:
            distances.append(distance)

        if visited[row][col]:
            continue

        visited[row][col] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc
            if is_valid_move(new_row, new_col, rows, cols, grid):
                queue.append((new_row, new_col, distance + 1))

    if len(distances) < 2:
        return -1

    distances.sort()
    return distances[-2]

# Input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
start_row, start_col = map(int, input().split())

# Find the second furthest treasure
distance = find_second_furthest_treasure(grid, start_row, start_col)

# Output
if distance == -1:
    print("we cannot reach two or more treasures")
else:
    print("second maximum distance:", distance)
