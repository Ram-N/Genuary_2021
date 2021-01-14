"""
GENUARY 2021 - "Do Not Repeat"
Use Tiles to create a non-repeating pattern

Ram Narasimhan
Jan13 2021

"""

from datetime import datetime
from grid import Grid
from rn_utils import pick_one

margin = 0
w, h = 960 + 2 * margin, 960 + 2 * margin

palette = [
    "#FE4019",  # orange
    "#36225E",  # dark blue
    "#e71d36",  # red
    "#0B85CF",  # light blue
    #    "#FF5FB9",  # pink
    "#2ec4b6",  # teal
    "#f69e55",  # orange
    "#FFA900",  # yellow
    "#ffffff",  # white
]


def render_background():
    ystep = 20
    num = height / ystep
    noStroke()
    for ry in range(int(num)):
        fill(ry, 31, 49, 150 - ry)
        rect(0, ry * ystep, width, ystep)


cell_mesh_sq = 8
JN_POINT = [2, cell_mesh_sq - 2]


def render_single_tile(c):
    """ render pattern in cell post rotation"""
    noFill()
    p1p, p2p, p3p, p4p = pick_one(jn_pairs)  # say (0,1) (2,3) (4, 7) (5,6)
    jxs, jys = c.gw * JN_POINT[0], c.gh * JN_POINT[0]
    jxl, jyl = c.gw * JN_POINT[1], c.gh * JN_POINT[1]

    jxc = [0, 0, jxs, jxl, c.width, c.width, jxl, jxs]
    jyc = [jyl, jys, 0, 0, jys, jyl, c.height, c.height]

    stroke("#36225E"),  # dark blue
    cx, cy = c.width / 2, c.height / 2
    cw2, ch2 = c.gw * 2, c.gh * 2
    strokeWeight(4)
    for idx, pp in enumerate([p1p, p2p, p3p, p4p]):
        ps, pe = pp
        xadj = c.gw * 2
        yadj = c.gh * 2

        if (pe - ps) == 2 or (pe - ps) == 3 or (pe - ps) == 6 or (pe - ps) == 7:
            xadj = (cx - jxc[ps]) / 2  # bz1
            yadj = (cy - jyc[ps]) / 2  # bz1
        bezier(
            jxc[ps],
            jyc[ps],
            cx - xadj,
            cy - yadj,
            cx + xadj,
            cy + yadj,
            jxc[pe],
            jyc[pe],
        )

    if random(1) > 0.4:
        fill("#36225E")
        ellipse(c.gw * 2, c.gh * 2, c.gh, c.gw)
        noFill()


def render_pattern_in_cell(c):

    # c.fill_cell(blue_shade)

    pushMatrix()
    translate(c.x, c.y)  # cell center
    rotate(PI / 2 * int(random(4)))
    translate(-c.width / 2, -c.height / 2)  # to cell nw corner
    render_single_tile(c)
    popMatrix()


jn_pairs = [
    ((1, 4), (3, 7), (2, 6), (0, 5)),
    ((1, 5), (3, 7), (4, 6), (0, 2)),
    ((0, 4), (2, 6), (1, 5), (3, 7)),
    ((0, 6), (2, 4), (1, 5), (3, 7)),
    ((0, 5), (1, 4), (2, 6), (3, 7)),
    ((0, 2), (1, 5), (4, 6), (3, 7)),
    ((0, 3), (1, 5), (4, 7), (2, 6)),
]


num_tiles = 8
g = Grid(num_tiles, num_tiles, w, h, 0, 0, cell_mesh_sq=8)

bg_color = 250


def setup():
    size(w, h)
    background(bg_color)
    stroke(124)
    g.render_cell_borders()

    # render_background()  # background

    for mi, c in enumerate(g.cells):  #
        # c.render_gridlines()
        render_pattern_in_cell(c)

    # draw_canvas_border(30, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "tiles1_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

