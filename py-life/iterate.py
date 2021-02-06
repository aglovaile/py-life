"""
Test file for life function
Prints the grid to the screen after every lifecycle
Will exit early if there's no alive cells on grid

:params (Class grid, int number of lifecycles, int delay for printing to screen)
"""

from time import sleep
from life import lifecycle


# Re[laces the 0 and 1 when printing the board
dark_icon = '░░'
med_icon = '▒▒'
light_icon ='▓▓'
board_prettify = {
    0: dark_icon,
    1: light_icon
}

def print_grid(grid):
    # TODO move this into the Grid class
    pretty_grid = grid.copy()
    for row in pretty_grid:
        print(''.join(list(map(lambda x: board_prettify[x], row))))

def check_if_alive(grid):
    """
    Checks for at least one alive cell in the grid
    """

    for i in range(grid.rows):
        for j in range(grid.cols):
            if grid.grid[i][j] == 1:
                return True
    return False

def iterate(grid, num, slp=.05):
    print_grid(grid.grid)
    for i in range(-1, num):
        if check_if_alive(grid):
            print('')
            lifecycle(grid)
            print_grid(grid.grid)
            sleep(slp)
        else:
            exit(0)