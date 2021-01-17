"""
GENUARY 2021 - "Circles Only"
Missing You.

Ram Narasimhan
Jan16 2021

"""

from datetime import datetime
from rn_utils import pick_one

margin = 30
w, h, = 1100, 1100  # working area
wm, hm = w + 2 * margin, h + 2 * margin  # total size


bg_color = 40
num_cols = 3
num_rows = 3

inter_cell = 50  # internal gap between 2 cells
cell_margin = 50  # initial gutter between canvas margin and the start of the first cell

cw = (w - 2 * cell_margin - (num_cols - 1) * inter_cell) / (num_cols)
ch = (h - 2 * cell_margin - (num_rows - 1) * inter_cell) / (num_rows)

print(w, h, cw, ch)


def render_panels():
    fill(20)
    noStroke()
    for yi in range(num_rows):
        for xi in range(num_cols):
            x, y = (
                margin + cell_margin + (inter_cell + cw) * xi,
                margin + cell_margin + (inter_cell + ch) * yi,
            )
            # rect(x, y, cw, ch)
            circle_pack(x, y, cw, ch)


MIN_RAD, MAX_RAD = 3, 35


def get_radius(x, y, circles, window_width, window_height):
    radius = MAX_RAD

    # check against the 4 walls
    min_d = min(x, y, window_width - x, window_height - y)
    if min_d < MIN_RAD:
        return 0
    if min_d < radius:
        radius = min_d

    for c in circles:
        d = dist(x, y, c.x, c.y)
        if d < c.radius + MIN_RAD:
            return 0
        if d < radius + c.radius:
            radius = d - c.radius

    return radius


color_p = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]


def circle_pack(wx, wy, window_width, window_height):
    circles = []
    pushStyle()
    fill(200)
    # stroke(200, 0, 0)
    pushMatrix()
    translate(wx, wy)
    done, failed = 0, 0
    while not done:
        x, y = random(window_width), random(window_height)
        radius = get_radius(x, y, circles, window_width, window_height)
        if radius:
            fill(pick_one(color_p))
            p = PVector(x, y)
            p.radius = radius
            circles.append(p)
            ellipse(x, y, 2 * radius, 2 * radius)
            failed = 0
        else:
            failed += 1

        if failed > 100:
            done = 1
    popMatrix()
    popStyle()


def setup():
    size(wm, hm)
    background(bg_color)

    render_panels()

    canvas_border = 30
    draw_canvas_border(canvas_border, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "circles_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wm, hm)

