"""
Generates a Grid class with a height and width relative to the size of the terminal
"""

from os import get_terminal_size


class Grid:

    _size = get_terminal_size()

    def __init__(self):
        self.grid = []
        self.cols = Grid._size.columns - 5
        self.rows = Grid._size.lines - 4

        for i in range(self.rows):
            tmp_row = [0] * self.cols
            self.grid.append(tmp_row)
