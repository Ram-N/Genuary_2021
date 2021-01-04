"""

Created for Genuary2021.
Something human.

Author: Ram Narasimhan

"""
from face import Face
from grid import Grid

w, h = 840, 840
cell_w, cell_h = w * 0.5, w * 0.5


def setup():
    size(w, h)
    cx, cy = 400, 400
    strokeWeight(2)
    fill(200, 0, 0)

    grid = Grid(1, 1, w, h, 20, 20)
    grid.render_grid_border()

    print(len(grid.cells))
    for c in grid.cells:
        print("cx", c.x, c.y)
        c.render_gridlines()
        pushMatrix()
        translate(c.x, c.y)  # go to cell's center
        radius = 140 + random(40)
        f = Face(0, 0, radius, c)
        f.draw_face(c)
        popMatrix()

    # for x in range(2):
    #     for y in range(2):
    #         cx = cell_w * 0.5 + cell_w * x
    #         cy = cell_h * 0.5 + cell_h * y
    #         print(cx, cy)
    #         pushMatrix()
    #         translate(cx, cy)
    #         radius = 40 + random(40)
    #         f = Face(0, 0, radius)
    #         f.draw_face()
    #         popMatrix()
