"""
GENUARY 2021 - "Subdivision"
Use Sphinx Tiles to Subdivide

Ram Narasimhan
Jan14 2021

"""

from datetime import datetime

margin = 0
w, h, = 960, 960
wm, hm = w + 2 * margin, h + 2 * margin


pal = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]


def render_background():
    ystep = 20
    num = height / ystep
    noStroke()
    for ry in range(int(num)):
        fill(ry, 31, 49, 150 - ry)
        rect(0, ry * ystep, width, ystep)


cell_mesh_sq = 8
JN_POINT = [2, cell_mesh_sq - 2]


# para 012, 234, 450 plus xy


def t_tile(x, y, orientation=0):

    pushMatrix()
    translate(x, y)

    rotate((orientation - 1) * TWO_PI / 6)

    beginShape()
    vertex(0, 0)
    vertex(0, th)
    vertex(tw, th / 2)
    endShape(CLOSE)
    popMatrix()


def parallelogram(x, y, orientation=0):

    pushMatrix()
    translate(x, y)

    if orientation == 2:
        rotate(TWO_PI / 3)
    elif orientation == 4:
        rotate(2 * TWO_PI / 3)

    beginShape()
    vertex(0, 0)
    vertex(0, th)
    vertex(tw, th / 2)
    vertex(tw, -th / 2)
    endShape(CLOSE)
    popMatrix()


def double_p(x, y, orientation=0):

    pushMatrix()
    translate(x, y)

    rotate((orientation + 4) * TWO_PI / 6)

    beginShape()
    vertex(0, 0)
    vertex(0, th)
    vertex(tw, th / 2)
    vertex(2 * tw, 0)
    vertex(2 * tw, -th)
    endShape(CLOSE)
    popMatrix()


def penta(x, y, orientation=0):

    pushMatrix()
    translate(x, y)

    rotate(orientation * TWO_PI / 6 + PI)

    vertices = [
        (0, 0),
        (-tw, th / 2),
        (0, th),
        (tw, th / 2),
        (2 * tw, 0),
        (2 * tw, -th),
    ]

    beginShape()
    for v in vertices:
        vertex(v)
    endShape(CLOSE)

    popMatrix()


def SShape(x, y, orientation=0):

    pushMatrix()
    translate(x, y)

    if orientation == 2:
        rotate(TWO_PI / 3)
    elif orientation == 4:
        rotate(2 * TWO_PI / 3)

    vertices = [
        (0, 0),
        (2 * tw, -th),
        (3 * tw, -th / 2),
        (2 * tw, 0),
        (5 * tw, 1.5 * th),
        (3 * tw, 2.5 * th),
        (2 * tw, 2 * th),
        (3 * tw, 1.5 * th),
    ]

    beginShape()
    for v in vertices:
        vertex(v)
    endShape(CLOSE)

    popMatrix()


def three_faced_hexagon(x, y, orientation=0):

    pushMatrix()
    translate(x, y)

    if orientation == 2:
        rotate(TWO_PI / 3)
    elif orientation == 4:
        rotate(2 * TWO_PI / 3)

    v1 = [(0, 0), (-tw / 2, -th), (tw / 2, -th), (tw, 0)]
    v2 = [(0, 0), (tw, 0), (0.5 * tw, th), (-0.5 * tw, th)]
    v3 = [(0, 0), (-tw / 2, th), (-tw, 0), (-0.5 * tw, -th)]

    col = [10, 100, 200]

    fill(col[0])
    beginShape()
    for v in v1:
        vertex(v)
    endShape(CLOSE)

    fill(col[1])
    beginShape()
    for v in v2:
        vertex(v)
    endShape(CLOSE)

    fill(col[2])
    beginShape()
    for v in v3:
        vertex(v)
    endShape(CLOSE)

    popMatrix()


def get_xy(cx, cy):
    return (dots[cx][cy].x, dots[cx][cy].y)


def interlocked_third(x, y, rot, _color):
    """ one third of the whole tile. One color"""

    h2, h3 = th * 2, th * 3
    w2, w3 = tw * 2, tw * 3

    pushMatrix()
    translate(x, y)
    rotate(rot * TWO_PI / 3)

    pushStyle()
    fill(_color)
    SShape(0, 0, 0)  # Top S
    parallelogram(-tw, th / 2, 4)  # Top P
    t_tile(w3, -th / 2, 0)  # top - T1
    double_p(tw * 6, -2 * th, 0)  # top double
    penta(w3, -2.5 * th, 0)
    # fill(100, 0, 0)
    if _color == pal[3]:
        fill("#e76f51")
    if _color == pal[2]:
        fill("#2a9d8f")

    parallelogram(2 * tw, 4 * th, 4)  # Top P

    popStyle()
    popMatrix()


def interlocked_tile(x0, y0):

    interlocked_third(x0, y0, 0, pal[2])
    rot = 1
    interlocked_third(x0 + 4 * tw, y0 - 3 * th, rot, pal[3])
    rot = 2
    interlocked_third(x0 + 5 * tw, y0 + 1.5 * th, rot, pal[0])


bg_color = 250

th = 30
tw = th * sqrt(3) / 2
num_cols = int(w / tw)
num_rows = int(2 * h / th)

dots = []
for col in range(num_cols):
    row_dots = []
    for row in range(num_rows):
        p = PVector()
        xoffset = 0 if row % 2 else tw
        x = col * tw * 2 + xoffset
        y = row * th / 2
        p.x, p.y = x, y
        p.row, p.col = row, col
        row_dots.append(p)
    dots.append(row_dots)


def setup():
    size(wm, hm)  # including margin
    background(bg_color)
    stroke(40)

    # for row in dots:
    #     for p in row:
    #         ellipse(p.x, p.y, 5, 5)
    print(num_rows, num_cols, len(dots))

    # x, y = get_xy(10, 10)
    # interlocked_tile(x, y)

    # draw all the tiles
    for row in range(-2, 7):
        yrow_offset = 6 * th * row
        xrow_offset = 2 * tw * row
        for col in range(-2, 7):
            x = xrow_offset + col * 7 * tw
            y = yrow_offset + 3.5 * th + 3 * col * th / 2
            interlocked_tile(x, y)

    draw_canvas_border(35, border_color="#2a9d8f")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "interlock_"
    save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

