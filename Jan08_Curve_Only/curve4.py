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
    "#FFA900",  # yellow
    "#a13e17",  # (161,62,23)
    "#cc000e",  # (204,0,14)
    #    "#ff0a0e",  # (255,10,14)
    "#fbc2b5",  # (251,194,181)
    #    "#fec196",  # (254,193,150)
    "#2ec4b6",  # teal
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


def flip():
    return 1 if (random(1) < 0.5) else -1


def render_opera(pair, g, fps):
    pa0, pa1 = pair
    ca0 = g.get_cell(pa0[0], pa0[1])
    ca1 = g.get_cell(pa1[0], pa1[1])
    cell_width = ca0.width

    flip1, flip2, flip3, flip4 = fps
    for e in range(NUM_ECHO):
        if e > 5:
            for symm in range(2):
                # flip = 1 if (sign % 2) else -1
                eps = e / (NUM_ECHO + 1.0)
                cw = cell_width * eps * 2
                bez1x = ca0.x + cw * flip1
                bez1y = ca0.y + cw * flip2
                bez2x = ca1.x + cw * flip3
                bez2y = ca1.y + cw * flip4
                bezier(ca0.x, ca0.y, bez1x, bez1y, bez2x, bez2y, ca1.x, ca1.y)
    # strokeWeight(2)
    # line(ca0.x, ca0.y, ca1.x, ca1.y)


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

    pairs = []
    col_ints = []
    flip_vec = []
    for pp in range(5):
        pairs.append(get_2pairs())
        col_ints.append(int(random(len(palette))))
        fps = (flip(), flip(), flip(), flip())
        flip_vec.append(fps)
    print(pairs)

    for rx, ry in ROTATIONS:
        pushMatrix()
        translate(width / 2, height / 2)
        scale(rx, ry)
        for _col, pair in enumerate(pairs):
            stroke(255)
            ellipse(10, 10, 100, 100)
            strokeWeight(3)
            # ellipse(0, 0, 100, 100)
            stroke(palette[col_ints[_col]])
            render_opera(pair, g, flip_vec[_col])
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
