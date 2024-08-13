from geometry import Cell
import time

class Maze:
    def __init__(
        self,
        x,
        y,
        rows,
        cols,
        cell_width,
        cell_height,
        win,
        seed=None
    ):
        self._x = x
        self._y = y
        self._rows = rows
        self._cols = cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = win
        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        self._draw_cell()
        self.seed = seed

    
    def _create_cells(self):
        list_of_cells = []
        y = self._y
        for _ in range(self._rows):
            cells = []
            x = self._x
            for _ in range(self._cols):
                cell = Cell(x, y, self._cell_width, self._cell_height, self._win)
                cells.append(cell)
                x += self._cell_width

            y += self._cell_height
            list_of_cells.append(cells)

        return list_of_cells



    def _draw_cell(self):
        if self._win is None:
            return
        lst = self._cells.copy()
        for ls in lst:
            for cell in ls:
                cell.draw()
                self._animate()



    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)



    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        self._cells[0][0] = Cell(entrance.x, entrance.y, self._cell_width, self._cell_height, self._win)
        self._cells[0][0].has_walls["top"] = False
        exit = self._cells[-1][-1]
        self._cells[-1][-1] = Cell(exit.x, exit.y, self._cell_width, self._cell_height, self._win)
        self._cells[-1][-1].has_walls["bottom"] = False


    def _break_walls_r(self):
        pass

            




