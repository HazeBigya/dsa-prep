def distinct_islands(grid):
    if not grid:
        return 0

    shapes = set()
    rows, cols = len(grid), len(grid[0])

    def flood(r, c, r0, c0, shape):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return

        grid[r][c] = 0
        shape.append((r - r0, c - c0))

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


print(
    distinct_islands(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
    )
)
