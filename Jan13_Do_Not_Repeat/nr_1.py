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
    p1p, p2p = pick_one(jn_pairs)  # say (0,1) (2,3)
    jx0, jy0 = c.gw * JN_POINT[0], c.gh * JN_POINT[0]
    jx1, jy1 = c.gw * JN_POINT[1], c.gh * JN_POINT[1]
    # print(c.nwx, c.nwy, "nw corner", c.gw, c.gh)
    # print(p1p, p2p, jx0, jy0, jx1, jy1, c.width, c.height)

    stroke("#001122")
    cx, cy = c.width / 2, c.height / 2
    cw2, ch2 = c.gw * 2, c.gh * 2
    for idx, jxy in enumerate([(jx0, jy0), (jx1, jy1)]):
        jx, jy = jxy
        # sw = 3 if idx else 6
        strokeWeight(4)
        if p1p == (0, 1):
            bezier(0, jy, cx, cy, cx, cy, c.width - jx, 0)  # 0 to 1
            bezier(c.width, c.height - jy, cx, cy, cx, cy, jx, c.height)  # 2 to 3
        if p1p == (0, 2):  # opposite sides
            bezier(
                0, jy, cx - cw2, cy - ch2, cx - cw2, cy - ch2, c.width, c.height - jy
            )  # 0 to 2
            bezier(
                c.width - jx, 0, cx + cw2, cy + ch2, cx + cw2, cy + ch2, jx, c.height
            )  # 1 to 3
        if p1p == (0, 3):
            bezier(0, jy, cx, cy, cx, cy, jx, c.height)  # 0 to 3
            bezier(c.width - jx, 0, cx, cy, cx, cy, c.width, c.height - jy)  # 1 to 2


def render_pattern_in_cell(c):

    # c.fill_cell(blue_shade)

    pushMatrix()
    translate(c.x, c.y)  # cell center
    rotate(PI / 2 * int(random(4)))
    translate(-c.width / 2, -c.height / 2)  # to cell nw corner
    render_single_tile(c)
    popMatrix()


bg_color = 120
num_tiles = 8

jn_pairs = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]

g = Grid(num_tiles, num_tiles, w, h, 0, 0, cell_mesh_sq=8)


def setup():
    size(w, h)
    stroke(240)
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

