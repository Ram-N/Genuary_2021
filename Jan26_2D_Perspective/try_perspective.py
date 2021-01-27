"""
GENUARY 2021 - "2D Perspective"

Ram Narasimhan
Jan26 2021
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
    size(wm, hm, P3D)  # including margin
    # # background(bg_color)
    # #    noStroke()
    # stroke(200)
    # col3 = [10, 100, 200]

    # Re-creates the default perspective
    #    size(100, 100, P3D)
    lights()
    fill("#ffc5c5")
    fov = PI / 3.0
    cameraZ = (height / 2.0) / tan(fov / 2.0)
    perspective(fov, float(width) / float(height), cameraZ / 10.0, cameraZ * 10.0)
    translate(width / 2, height * 0.75, 0)
    rotateX(-PI / 6)
    rotateY(PI / 6)
    directionalLight(0, 255, 0, 0, -1, 0)
    box(100)

    # draw_canvas_border(40, border_color=bg_color)
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # titlestr = "perspective_"
    # save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

