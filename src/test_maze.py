import unittest
from maze import Maze

class TestMaze(unittest.TestCase):

    def test_maze_create_cell(self):
        cols = 12
        rows = 10
        m1 = Maze(0, 0, rows, cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            rows
        )
        self.assertEqual(
            len(m1._cells[0]),
            cols
        )


    def test_maze_reset_visited(self):
        cols = 12
        rows = 10
        m1 = Maze(0, 0, rows, cols, 10, 10, None)
        for row in m1._cells:
            for col in row:
                self.assertFalse(col.visited)





if __name__ == "__main__":
    unittest.main()

