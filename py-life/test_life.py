"""
Test file for the life and iterate functions
Profiles the runtime after completion
"""


import os
from pprint import pprint
from iterate import iterate
from grid import Grid


glider = [
    [0,1,0],
    [0,0,1],
    [1,1,1]
]


def fill_grid(shape, grid, x_offset=0, y_offset=0):
    shape_w = len(shape[0])
    shape_h = len(shape)
    for r in range(shape_h):
        for c in range(shape_w):
            print(f'row: {r} col: {c} value: {shape[r][c]}')
            grid.grid[r + y_offset][c + x_offset] = shape[r][c]
        print(grid.grid[r])


def main():
    #new_grid = gen_grid()
    new_grid = Grid()
    fill_grid(glider, new_grid, 20)
    iterate(new_grid, 111)


if __name__ == '__main__':
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()
