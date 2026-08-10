def numDistinctIslands(grid):
    if not grid:
        return 0

    shapes = set()
    rows, cols = len(grid), len(grid[0])

    def flood(r, c, r0, c0, shape):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return

        shape.append((r - r0, c - c0))
        grid[r][c] = 0

        flood(r + 1, c, r0, c0, shape)
        flood(r - 1, c, r0, c0, shape)
        flood(r, c + 1, r0, c0, shape)
        flood(r, c - 1, r0, c0, shape)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                shape = []
                flood(r, c, r, c, shape)
                shapes.add(tuple(shape))

    return len(shapes)


# NOTE: flood mutates the grid (sinks 1 -> 0), so each test needs a FRESH grid.

# Test 1 — two identical 2x2 squares in different spots -> 1
print(
    numDistinctIslands(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
    )
)  # want 1

# Test 2 — mixed shapes -> 3
print(
    numDistinctIslands(
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1],
        ]
    )
)  # want 3

# Test 3 — one island -> 1
print(
    numDistinctIslands(
        [
            [1, 1, 0],
            [0, 1, 1],
        ]
    )
)  # want 1

# Test 4 — all water -> 0
print(
    numDistinctIslands(
        [
            [0, 0],
            [0, 0],
        ]
    )
)  # want 0

# Test 5 — four single cells (all same 1x1 shape) -> 1
print(
    numDistinctIslands(
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]
    )
)  # want 1

# Test 6 — same shape, one shifted: an L and the same L elsewhere -> 1
print(
    numDistinctIslands(
        [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
        ]
    )
)  # want 1
