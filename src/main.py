from geometry import Cell
from maze import Maze
from window import Window

def test_draw_cell(window):
    cell = Cell(10, 10, 50, 50, window)
    cell.draw()
    cell2 = Cell(10, 60, 50, 50, window)
    cell2.draw()

    cell.draw_move(cell2)


def main():
    rows = 12
    cols = 16
    margin = 50
    screen_width = 800
    screen_height = 600
    cell_width = (screen_width - 2 * margin) / cols
    cell_height = (screen_height - 2 * margin) / rows

    window = Window(screen_width, screen_height, "Test")

    Maze(margin, margin, 12, 16, cell_width, cell_height, window)


    window.wait_for_close()



main()
