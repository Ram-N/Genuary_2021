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
    "#0B85CF",  # light blue
    # "#FF5FB9",  # pink
    # "#2ec4b6",  # teal
    "#FFA900",  # yellow
    "#e71d36",  # red
    # "#ffffff",  # white
    # "#36225E",  # dark blue
]

# Colour Blocking 3 Color Palette
palette = [
    #    "#ff0a0e",  # (255,10,14) # red
    "#2ec4b6",  # teal
    "#cc000e",  # (204,0,14) # red3
    "#fbc2b5",  # (251,194,181) # pastel
    "#FFA900",  # yellow
    "#f69e55",  # orange
    "#a13e17",  # (161,62,23) # brown
    "#FFA900",  # yellow
    "#fbc2b5",  # (251,194,181) # pastel
    #    "#fec196",  # (254,193,150)
]


w = 1040
margin = 20


# random colors, but fixed
col_ints = [int(random(len(palette))) for _ in range(20)]
col_int = int(random(len(palette)))


def get_2pairs():
    """x y and x+1, y or x and y+1"""

    done = 0
    while not done:

        r0 = 1 + int(random(GRID_CELLS // 2 - 1))
        c0 = 1 + int(random(GRID_CELLS // 2 - 1))

        r1 = 1 + int(random(GRID_CELLS // 2 - 1))
        c1 = 1 + int(random(GRID_CELLS // 2 - 1))
        done = 1
        print(r0, c0, r1, c1)
        if r1 == r0:
            if c1 == c0:
                done = 0
        elif (c1 - c0) / (r1 - r0) == 1:
            done = 0
    return ((r0, c0), (r1, c1))


def old_get_pairs():
    done = 0
    while not done:

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


def render_opera(pair, g, decider):
    pa0, pa1 = pair
    ca0 = g.get_cell(pa0[0], pa0[1])
    ca1 = g.get_cell(pa1[0], pa1[1])
    cell_width = ca0.width

    if decider < 0.6:
        for e in range(NUM_ECHO):
            if e > 5:
                for sign in range(2):
                    flip = 1 if (sign % 2) else -1
                    eps = e / (NUM_ECHO + 1.0)
                    cw = cell_width * eps * 2
                    bez1x = ca0.x - cw * flip
                    bez1y = ca0.y - cw * flip
                    bez2x = ca1.x - cw * flip
                    bez2y = ca1.y - cw * flip
                    bezier(ca0.x, ca0.y, bez1x, bez1y, bez2x, bez2y, ca1.x, ca1.y)

    elif decider < 0.7:
        for e in range(NUM_ECHO):
            if e > 5:
                for sign in range(2):
                    flip = 1 if (sign % 2) else -1
                    eps = e / (NUM_ECHO + 1.0)
                    cw = cell_width * eps * 2
                    bez1x = ca0.x - cw * flip
                    bez1y = ca0.y - cw * flip
                    bez2x = ca1.x + cw * flip
                    bez2y = ca1.y + cw * flip
                    bezier(ca0.x, ca0.y, bez1x, bez1y, bez2x, bez2y, ca1.x, ca1.y)
    elif decider < 0.81:
        for e in range(NUM_ECHO):
            if e > 5:
                for sign in range(2):
                    flip = 1 if (sign % 2) else -1
                    eps = e / (NUM_ECHO + 1.0)
                    cw = cell_width * eps * 2
                    bez1x = ca0.x + cw * flip
                    bez1y = ca0.y + cw * flip
                    bez2x = ca1.x - cw * flip
                    bez2y = ca1.y - cw * flip
                    bezier(ca0.x, ca0.y, bez1x, bez1y, bez2x, bez2y, ca1.x, ca1.y)

    else:
        for e in range(NUM_ECHO):
            if e > 5:
                for sign in range(2):
                    flip = 1 if (sign % 2) else -1
                    eps = e / (NUM_ECHO + 1.0)
                    cw = cell_width * eps * 2
                    bez1x = ca0.x + cw * flip
                    bez1y = ca0.y + cw * flip
                    bez2x = ca1.x + cw * flip
                    bez2y = ca1.y + cw * flip
                    bezier(ca0.x, ca0.y, bez1x, bez1y, bez2x, bez2y, ca1.x, ca1.y)


GRID_CELLS = 11
NUM_ECHO = 12


def setup():
    size(w, w)
    background(10)
    noFill()
    stroke(200)
    strokeWeight(1)

    # let's lay out a simple Grid
    g = Grid(GRID_CELLS, GRID_CELLS, w, w)
    #    g.render_cell_centers()
    #    g.render_cell_borders()

    pairs = [
        #        ((1, 1), (1, 2)),
        ((2, 3), (2, 4)),
        ((2, 2), (1, 4)),
        ((3, 1), (3, 4)),
        ((1, 2), (3, 1)),
        ((4, 4), (3, 1)),
    ]

    print(pairs)

    dec = [0.65, 0.9, 0.1, 0.9, 0.88]

    for _col, pair in enumerate(pairs):
        decider = dec[_col]
        for rx, ry in ROTATIONS:
            pushMatrix()
            translate(width / 2, height / 2)
            scale(rx, ry)
            stroke(255)
            ellipse(10, 10, 100, 100)
            strokeWeight(3)
            stroke(palette[_col])
            render_opera(pair, g, decider)
            popMatrix()

    titlestr = "2curves"
    draw_canvas_border(20)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    titlestr = "curves_"
    save("images/" + titlestr + coda + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, w)
