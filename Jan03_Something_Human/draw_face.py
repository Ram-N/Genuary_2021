"""

Created for Genuary2021.
Something human.

Author: Ram Narasimhan

"""
from face import Face
from grid import Grid

w, h = 840, 840
cell_w, cell_h = w * 0.5, w * 0.5


grid = Grid(1, 1, w, h, 20, 20)
grid = Grid(5, 5, w, h, 20, 20)


def setup():
    size(w, h)
    frameRate(1)
    grid.render_grid_border()


def draw():
    background(255)
    for c in grid.cells:
        # c.render_gridlines()
        pushMatrix()
        translate(c.x, c.y)  # go to cell's center
        f = Face(0, 0, c)
        f.draw_face(c)
        popMatrix()
    saveFrame("images/g25_###.png")

    if frameCount > 25:
        noLoop()
