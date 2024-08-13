from geometry import Cell
import time
import random

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
        self.seed = seed
        if self.seed != None:
            random.seed(self.seed)
        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(self._cells, 0, 0)
        self._reset_visited_property()
        self._draw_cell()

    
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


    def _break_walls_r(self, cells, i, j):
        cells[i][j].visited = True
        while True:
            available_node = []
            for val in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                if 0 <= val[0] < len(cells) and 0 <= val[1] < len(cells[0]):
                    if not cells[val[0]][val[1]].visited:
                        available_node.append(val)

            if not available_node:
                return


            rand_index = random.choice(available_node)
            chosen_direction = self.__direction_indicator(i, j, rand_index)
            cells[i][j].has_walls[chosen_direction] = False
            cells[rand_index[0]][rand_index[1]].has_walls[self.__opposite_direction(chosen_direction)] = False
            self._break_walls_r(cells, rand_index[0], rand_index[1])


    def __opposite_direction(self, direction):
        oppo = {
            "top": "bottom",
            "left": "right",
            "bottom": "top",
            "right": "left"
        }
        return oppo[direction]


    
    def __direction_indicator(self, i, j, val):
        direction = {
            (i-1, j): "top",
            (i, j+1): "right",
            (i+1, j): "bottom",
            (i, j-1): "left"
        }
        return direction[val]


    def _reset_visited_property(self):
        for row in range(len(self._cells)):
            for col in range(len(self._cells[0])):
                self._cells[row][col].visited = False


    def solve(self):
        solved = self._solve_r(0, 0)
        return solved


    def _solve_r(self, i, j):
        self._animate()
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True


        for direction in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if 0 <= direction[0] < len(self._cells) and 0 <= direction[1] < len(self._cells[0]):
                adjacent_cell = self._cells[direction[0]][direction[1]]
                chosen_dir = self.__direction_indicator(i, j, direction)
                if (
                    adjacent_cell.has_walls[self.__opposite_direction(chosen_dir)] == False
                    and adjacent_cell.visited == False
                    and self._cells[i][j].has_walls[chosen_dir] == False
                ):
                    self._cells[i][j].draw_move(adjacent_cell)
                    self._cells[i][j].visited = True
                    res = self._solve_r(direction[0], direction[1])
                    if res:
                        return True
                    else:
                        self._cells[i][j].draw_move(adjacent_cell, undo=True)

