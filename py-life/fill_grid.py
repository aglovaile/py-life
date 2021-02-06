def fill_grid(shape, grid, x_offset=0, y_offset=0):
    shape_w = len(shape[0])
    shape_h = len(shape)
    for r in range(shape_h):
        for c in range(shape_w):
            print(f'row: {r} col: {c} value: {shape[r][c]}')
            grid.grid[r + y_offset][c + x_offset] = shape[r][c]
        print(grid.grid[r])