"""
GENUARY 2021 - "Grid of Permutations"
Shapes on a Hexagonal Grid

Ram Narasimhan
Jan25 2021
"""

from datetime import datetime
from math import sqrt

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

    ellipse(0, 0, 4, 4)

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


def three_faced_hexagon(x, y, orientation=0, hw=1, hh=1, col=[10, 50, 80], rnd_flag=0):

    pushMatrix()
    translate(x, y)

    rotate(orientation * TWO_PI / 6)

    center = (0, 0)
    v0, v1 = (hw, -hh / 2), (hw, hh / 2)
    v2, v3 = (0, hh), (-hw, hh / 2)
    v4, v5 = (-hw, -hh / 2), (0, -hh)

    vers1 = [center, v0, v1, v2]
    vers2 = [center, v2, v3, v4]
    vers3 = [center, v4, v5, v0]

    ellipse(0, 0, 10, 10)

    col3 = col
    if rnd_flag:
        col3 = []
        done = 0
        while not done:
            new = int(random(len(col)))
            if col[new] not in col3:
                col3.append(col[new])

            if len(col3) == 3:
                done = 1

    fill(col3[0])
    beginShape()
    for v in vers1:
        vertex(v)
    endShape(CLOSE)

    fill(col3[1])
    beginShape()
    for v in vers2:
        vertex(v)
    endShape(CLOSE)

    fill(col3[2])
    beginShape()
    for v in vers3:
        vertex(v)
    endShape(CLOSE)

    if random(1) < 0.25:
        fill(230)
        ellipse(10, 10, 10, 10)
    if random(1) < 0.25:
        fill(170)
        ellipse(-10, 10, 10, 10)
    popMatrix()


def get_xy(cx, cy):
    return (dots[cx][cy].x, dots[cx][cy].y)


th = 80
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

bg_color = 25


def setup():
    size(wm, hm)  # including margin
    background(bg_color)
    noStroke()

    col3 = [10, 100, 200]

    for col in range(0, num_cols):
        for row in range(1, num_rows, 3):
            x, y = get_xy(col, row)
            hw, hh = 0.87 * tw, 0.87 * th
            col3 = ["#5e60ce", "#5390d9", "#4ea8de", "#48bfe3", "#56cfe1"]
            rot = random(6)
            three_faced_hexagon(x, y, rot, hw, hh, col3, 0)
            rot = random(6)
            col3 = [
                "#6a040f",
                "#9d0208",
                "#d00000",
                "#dc2f02",
                "#e85d04",
                "#f48c06",
                "#faa307",
                "#ffba08",
            ]
            hw, hh = 0.4 * tw, 0.4 * th
            three_faced_hexagon(x, y, rot, hw, hh, col3, rnd_flag=1)

    draw_canvas_border(40, border_color=bg_color)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "permutations_"
    save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

