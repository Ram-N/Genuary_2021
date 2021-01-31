"""
GENUARY 2021 - "Any Shape, none can touch"

Ram Narasimhan
Jan29 2021

"""

from datetime import datetime
from shapes import circle_pack

margin = 30
w, h, = 1020, 1020  # working area
wm, hm = w + 2 * margin, h + 2 * margin  # total size


color_p = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]


def render_circles(circles):

    fill(random(255), random(255), random(255))
    for c in circles:
        ellipse(c.x, c.y, 2 * c.radius, 2 * c.radius)


num_cols = 1
num_rows = 1


def render_panels():

    inter_cell = 50  # internal gap between 2 cells
    cell_margin = (
        50
    )  # initial gutter between canvas margin and the start of the first cell

    cw = (w - 2 * cell_margin - (num_cols - 1) * inter_cell) / (num_cols)
    ch = (h - 2 * cell_margin - (num_rows - 1) * inter_cell) / (num_rows)

    print(w, h, cw, ch)

    fill(20)
    noStroke()
    for yi in range(num_rows):
        for xi in range(num_cols):
            x, y = (
                margin + cell_margin + (inter_cell + cw) * xi,
                margin + cell_margin + (inter_cell + ch) * yi,
            )
            rect(x, y, cw, ch)
            circles = circle_pack(x, y, cw, ch)

            render_circles(circles)


bg_color = 40


def setup():
    size(wm, hm)
    background(bg_color)

    render_panels()

    canvas_border = 30
    draw_canvas_border(canvas_border, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "shapes_"
    save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wm, hm)

