from geometry import Cell
from window import Window

def main():
    window = Window(800, 600, "Test")
    cell = Cell(10, 10, 20, 20, window)
    cell.draw()
    cell2 = Cell(10, 50, 20, 20, window)
    cell2.draw(walls=["left", "top", "right"])
    cell3 = Cell(10, 90, 20, 20, window)
    cell3.draw(walls=["top", "right", "bottom"])
    cell4 = Cell(10, 130, 20, 20, window)
    cell4.draw(walls=["right", "left"])
    window.wait_for_close()



main()
