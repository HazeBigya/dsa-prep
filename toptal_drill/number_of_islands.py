def num_island(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def flood(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        grid[r][c] = "0"
        flood(r + 1, c)
        flood(r - 1, c)
        flood(r, c + 1)
        flood(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                flood(r, c)

    return count


# Test 1 — your 2x2 block + lone island → 2
grid1 = [
    ["1", "1", "0"],
    ["1", "1", "0"],
    ["0", "0", "1"],
]
print(num_island(grid1))  # want 2

# Test 2 — one big connected island → 1
grid2 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(num_island(grid2))  # want 1

# Test 3 — classic, 3 separate islands → 3
grid3 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(num_island(grid3))  # want 3

# Test 4 — all water → 0
grid4 = [
    ["0", "0"],
    ["0", "0"],
]
print(num_island(grid4))  # want 0

# Test 5 — diagonal touch does NOT connect → 2
grid5 = [
    ["1", "0"],
    ["0", "1"],
]
print(num_island(grid5))  # want 2

# Test 6 — single cell → 1
grid6 = [["1"]]
print(num_island(grid6))  # want 1
