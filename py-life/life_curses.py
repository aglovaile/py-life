import curses
from grid import Grid
from fill_grid import fill_grid
from life import lifecycle
  
glider = [
    [0,1,0],
    [0,0,1],
    [1,1,1]
]

reflector = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

new_grid = Grid()
fill_grid(reflector, new_grid, 20, 10)

grid_length = 60
grid_height = 50
window_width = new_grid.cols + 1
window_height = new_grid.rows + 1
sleep_time = 50

iterations = 300



screen = curses.initscr()
window = curses.newwin(window_height, window_width, 0, 0)

curses.start_color()
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

colors = {
    0: curses.color_pair(2),
    1: curses.color_pair(1)
}


def draw_grid():
    for i in range(new_grid.rows):
        for j in range(new_grid.cols):
            value = new_grid.grid[i][j]
            window.addstr(i, j, str(value), colors[value])


def draw_life(stdstr):

    for i in range(iterations):
        draw_grid()
        window.refresh()
        curses.napms(sleep_time)
        lifecycle(new_grid)


    curses.napms(2000)
    window.clear()
 
    curses.endwin()

def main():
    curses.wrapper(draw_life)

if __name__ == "__main__":
    main()


print('Window ended.')