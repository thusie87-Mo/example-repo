def count_adjacent_mines(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Directions: 8 surrounding cells (horizontal, vertical, diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    # Create a new grid to store the result
    result = []

    for i in range(rows):
        row_result = []
        for j in range(cols):
            if grid[i][j] == "#":
                row_result.append("#")
            else:
                count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "#":
                        count += 1
                row_result.append(str(count))
        result.append(row_result)  # This was missing
    return result  # Moved outside the loop

# Sample input
input_grid = [
    ["_", "_", "_", "#", "#"],
    ["_", "#", "_", "_", "_"],
    ["_", "_", "#", "_", "_"],
    ["_", "#", "#", "_", "_"],
    ["_", "_", "_", "_", "_"]
]

# Output
output_grid = count_adjacent_mines(input_grid)
for row in output_grid:
    print(" ".join(row))
