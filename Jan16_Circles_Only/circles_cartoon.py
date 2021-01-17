"""
GENUARY 2021 - "Circles Only"
Missing You.

Ram Narasimhan
Jan16 2021

"""

from datetime import datetime

margin = 30
w, h, = 950, 450  # working area
wm, hm = w + 2 * margin, h + 2 * margin  # total size


bg_color = 210
ts = 50
num_cols = 2
num_rows = 1

inter_cell = 50  # internal gap between 2 cells
cell_margin = 0  # initial gutter between canvas margin and the start of the first cell

cw = (w - 2 * cell_margin - (num_cols - 1) * inter_cell) / (num_cols)
ch = (h - 2 * cell_margin - (num_rows - 1) * inter_cell) / (num_rows)

print(w, h, cw, ch)

ball_rows = 5
ball_cols = 9
radius = 30
gap = 17
shelf_gap = 70


def render_2_panels():
    fill(20)
    noStroke()
    for yi in range(num_rows):
        for xi in range(num_cols):
            x, y = (
                margin + cell_margin + (inter_cell + cw) * xi,
                margin + cell_margin + (inter_cell + ch) * yi,
            )
            rect(x, y, cw, ch)

    for shelf in range(2):

        bx_offset = margin + cell_margin + 30 + 500 * shelf
        by_offset = margin + cell_margin + 30
        fill(250)
        for bx in range(ball_cols):
            for by in range(ball_rows):
                x = bx * (radius + gap) + bx_offset
                y = by * (radius + shelf_gap) + by_offset
                if (bx, by) == (6, 3):
                    if not shelf:
                        ellipse(x, y - 10, 50, 50)
                else:
                    ellipse(x, y, 30, 30)


def setup():
    size(wm, hm)
    background(bg_color)

    render_2_panels()

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

