"""
Created for Genuary2021
Jan 08 - Curve Only
Author: Ram Narasimhan

Steps
0. Let a simple rectangular grid. Dots
1. Pick 2 points. Bezier them. Offset and Bezier again.
2. Move to another set of 2 points.
"""

from grid import Grid, ROTATIONS


palette = [
    "#FE4019",  # orange
    "#36225E",  # dark blue
    "#0B85CF",  # light blue
    "#e71d36",  # red
    "#ffffff",  # white
    "#FFA900",  # yellow
]

w = 1040
margin = 20


# random colors, but fixed
col_ints = [int(random(len(palette))) for _ in range(20)]


def get_2pairs():
    """x y and x+1, y or x and y+1"""

    done = 0
    while not done:
        r0 = int(random(GRID_CELLS))
        c0 = int(random(GRID_CELLS))

        r1 = int(random(GRID_CELLS))
        c1 = int(random(GRID_CELLS))
        done = 1

        if random(1) < 0.5:
            # move one cell right
            ra1 = r0 + 1
            rb1 = r1 + 1
            ra0, rb0 = r0, r1
            ca0, cb0 = c0, c1
            ca1, cb1 = c0, c1

            if ra1 >= GRID_CELLS or rb1 >= GRID_CELLS:
                done = 0
        else:  # move down:
            ca1 = c0 + 1
            cb1 = c1 + 1
            ca0, cb0 = c0, c1
            ra0, rb0 = r0, r1
            ra1, rb1 = r0, r1
            if ca1 >= GRID_CELLS or cb1 >= GRID_CELLS:
                done = 0

    return [((ra0, ca0), (rb0, cb0)), ((ra1, ca1), (rb1, cb1))]


def render_opera(pair, g):
    pa0, pa1 = (1, 1), (0, 3)
    ca0 = g.get_cell(pa0[0], pa0[1])
    ca1 = g.get_cell(pa1[0], pa1[1])
    cell_width = ca0.width

    for e in range(NUM_ECHO):
        if e > 5:
            for sign in range(2):
                flip = 1 if (sign % 2) else -1
                eps = e / (NUM_ECHO + 1.0)
                cw = cell_width * eps
                bez1x = ca0.x - cw * flip
                bez1y = ca0.y - cw * flip
                bez2x = ca1.x - cw * flip
                bez2y = ca1.y - cw * flip
                bezier(ca0.x, ca0.y, bez1x, bez1y, bez2x, bez2y, ca1.x, ca1.y)


GRID_CELLS = 10
NUM_ECHO = 12


def setup():
    size(w, w)
    background(10)
    noFill()
    stroke(200)
    strokeWeight(1)

    # let's lay out a simple Grid
    g = Grid(10, 10, w, w)
    g.render_cell_centers()

    pairs = [((1, 1), (0, 3))]
    for rx, ry in ROTATIONS:
        pushMatrix()
        translate(width / 2, height / 2)
        scale(rx, ry)
        for pair in pairs:
            print(rx, ry)

            ellipse(10, 10, 100, 100)
            render_opera(pair, g)
        popMatrix()

    titlestr = "curves"
    draw_canvas_border(20)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    titlestr = "code_golf_"
    # save("images/" + titlestr + coda + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, w)
