"""
Game of Life lifecycle
- Takes a Grid class and modifies its grid property to be one lifecyle +1
- Each row of the grid must be equal in length
- Each row entry must be either 1 or 0

Grid class:
- grid: List[List[int]]
- rows: int
- cols: int
"""


def lifecycle(grid) -> None:
    """
    :param grid: List[List[int]] A 2d array of ints describing the boardstate
    :returns None:

    Starts with an empty list of changes to apply
    Applies rules on each cell and pushes items for changing
    Finally modifies the grid with each change in changes list
    """
    
    changes = []
    
    for [i,j] in check_for_neighbors(grid):
        n_count = count_neighbors(grid, i, j)
        if grid.grid[i][j] == 1:
            if n_count < 2 or n_count > 3:
                changes.append([[i,j], 0])
        else:
            if n_count == 3:
                changes.append([[i,j], 1])

    for change in changes:
        y = change[0][0]
        x = change[0][1]
        grid.grid[y][x] = change[1]


def get_neighbors(grid, y, x):
    """
    Returns a list of all cells in a 3x3 square around [y,x]
    """

    min_y = y - 1 if y - 1 >= 0 else 0
    min_x = x - 1 if x - 1 >= 0 else 0
    max_y = y + 2 if y + 1 < grid.rows else y + 1
    max_x = x + 2 if x + 1 < grid.cols else x + 1
    neighbors = []

    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            if [i,j] != [y,x]:
                neighbors.append([i,j])

    return neighbors
 

def check_for_neighbors(grid):
    """
    Returns a list of all cells whose state needs to be checked in the lifecycle
    Only cells who equal 1 or touch a cell equal to one need to be checked
    """

    check_list = []
    for i in range(grid.rows):
        for j in range(grid.cols):
            if grid.grid[i][j] == 1:
                neighbors = get_neighbors(grid, i, j)
                for cell in neighbors:
                    if cell not in check_list:
                        check_list.append(cell)
                if [i,j] not in check_list:
                    check_list.append([i,j])

    return check_list


def count_neighbors(grid, y, x):
    """
    Checks for number of alive cells in a 3x3 grid around index [y,x]
    """

    neighbors = get_neighbors(grid, y, x)
    count = 0

    for cell in neighbors:
        i = cell[0]
        j = cell[1]
        if grid.grid[i][j] == 1:
            count += 1
    
    return count