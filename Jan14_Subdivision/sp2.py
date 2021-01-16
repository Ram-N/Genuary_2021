"""
GENUARY 2021 - "Subdivision"
Use Sphinx Tiles to Subdivide

Ram Narasimhan
Jan14 2021

"""

from datetime import datetime
from grid import Grid
from rn_utils import pick_one

margin = 0
w, h, = 960, 960
wm, hm = w + 2 * margin, h + 2 * margin

palette = [
    "#FE4019",  # orange
    "#36225E",  # dark blue
    "#e71d36",  # red
    "#0B85CF",  # light blue
    "#FF5FB9",  # pink
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


def draw_sphinx((x0,y0), orientation='R', size=1, _rotation=3,  flip=False, fc=None):
    """

        _rotation in integer sets of 60 degrees. 0 to 5
    """

    sw, sh = tw * size, th * size

    pushStyle()
    if fc:
        fill(fc)

    flip = -1 if orientation=='L' else 1

    pushMatrix()
    translate(x0, y0)
    rotate(_rotation * PI / 3)
    x1, y1 = sw * flip, 2 * sh
    x2, y2 = 1.5 * sw * flip, sh
    x3, y3 = 2.5 * sw * flip, sh
    x4, y4 = 3 * sw * flip, 0


    beginShape()
    vertex(0, 0)
    vertex(x1, y1)
    vertex(x2, y2)
    vertex(x3, y3)
    vertex(x4, y4)
    endShape(CLOSE)

    popMatrix()
    popStyle()


bg_color = 250

tw = 50
th = tw * cos(PI / 6)

num_cols = int(w / tw)
num_rows = int(h / th)


def subdivide(chirality, orientation, (x0,y0), size):
    """
    Subdivide a Sphinx of given chirality, orientation based at x0, y0 of size into 4 smaller sphinxes.
    Return their properties (Chiral, orient, base, size)
    """

    pushMatrix()
    translate(x0, y0)

    # x1, y1 = x0+ 3 * size*tw, y0
    # x2, y2 = x0 - size*tw, y0 - 2*size*th
    # x3, y3 = x0 - size*tw, y0 - 4*size*th
    x1, y1 = 3 * size*tw, 0
    x2, y2 = -size*tw, -2*size*th
    x3, y3 = -size*tw, -4*size*th

    draw_sphinx((0,0), size=size, fc="#ff00ff")  # start
    draw_sphinx((x1,y1), size=size, fc=120)  # east of start
    draw_sphinx((x2,y2), size=size, _rotation=0)  # upside down
    draw_sphinx((x3,y3), 'L', size=size, _rotation=5,fc="#123456") #base is at peak point



    popMatrix()

def setup():
    size(wm, hm)  # including margin
    background(bg_color)
    stroke(40)

    dots = []
    for col in range(num_cols):
        row_dots = []
        for row in range(num_rows):
            p = PVector()
            xoffset = 0 if row % 2 else tw / 2
            x = col * tw + xoffset
            y = row * th
            ellipse(x, y, 5, 5)
            p.x, p.y = x, y
            p.row, p.col = row, col
            row_dots.append(p)
        dots.append(row_dots)

    print(num_rows, num_cols, len(dots))

    sx, sy = 10, 19
    size = 3
    x0, y0 = dots[sx][sy].x, dots[sx][sy].y
    subdivide('L', 3, (x0,y0), size)

    # draw_canvas_border(30, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "sphinx1_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

