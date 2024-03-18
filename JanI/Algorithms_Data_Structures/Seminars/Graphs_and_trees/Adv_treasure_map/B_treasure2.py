def is_valid_move(row, col, rows, cols, grid):
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

def find_nearest_treasure(grid, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])
    min_distance = float('inf')

    def backtrack(row, col, distance):
        nonlocal min_distance

        if grid[row][col] == 't':
            min_distance = min(min_distance, distance)
            return

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc
            if is_valid_move(new_row, new_col, rows, cols, grid):
                grid[row][col] = 'X'  # Mark the cell as visited to avoid revisiting
                backtrack(new_row, new_col, distance + 1)
                grid[row][col] = '.'  # Restore the cell to its original state after backtracking

    backtrack(start_row - 1, start_col - 1, 0)

    return min_distance if min_distance != float('inf') else -1

# Input
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
start_row, start_col = map(int, input().split())

# Find the nearest treasure using backtracking
distance = find_nearest_treasure(grid, start_row, start_col)

# Output
if distance == -1:
    print("no treasure can be reached")
else:
    print("minimum distance:", distance)
