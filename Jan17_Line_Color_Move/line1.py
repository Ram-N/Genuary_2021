"""
GENUARY 2021 - "Draw A line, pick a color, move a bit"

Ram Narasimhan
Jan17 2021

"""

from datetime import datetime
from rn_utils import pick_one

canvas_margin = 30
w, h, = 1080, 1080  # working area
wm, hm = w + 2 * canvas_margin, h + 2 * canvas_margin  # total size


bg_color = 40

# Panels
panel_cols = 2
panel_rows = 2

inter_cell = 30  # internal gap between 2 panels
cell_margin = 30  # initial gutter between canvas margin & the start of the first panel

pw = (w - 2 * cell_margin - (panel_cols - 1) * inter_cell) / (panel_cols)
ph = (h - 2 * cell_margin - (panel_rows - 1) * inter_cell) / (panel_rows)

print(w, h, pw, ph)


def render_panels():
    fill(100)
    noStroke()
    for yi in range(panel_rows):
        for xi in range(panel_cols):
            x, y = (
                canvas_margin + cell_margin + (inter_cell + pw) * xi,
                canvas_margin + cell_margin + (inter_cell + ph) * yi,
            )
            #            rect(x, y, pw, ph)
            draw_lines(x, y, pw, ph)  # inside panel
            print(x, y)


color_p = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
color_p = [
    #    "#264653",
    "#2a9d8f",
    "#e9c46a",
    "#f4a261",
    "#e76f51",
]


def draw_lines(wx, wy, panel_width, panel_height):
    pushStyle()
    fill(200)
    strokeWeight(2)
    pushMatrix()
    translate(wx, wy)
    y, ystep = 0, 5
    col = 0
    x = random(panel_width)
    while not y > panel_height:
        stroke(color_p[col % len(color_p)])
        # lw = random(panel_width)
        lw = (col * 5) % panel_width
        if x + lw > panel_width:
            line(min(x, panel_width), y, panel_width, y)
            line(0, y, min(x + lw - panel_width, panel_width), y)
            x = x + lw - panel_width
        else:
            line(x, y, x + lw, y)
            x = x + lw
        y += ystep
        col += 1
    popMatrix()
    popStyle()


def setup():
    size(wm, hm)
    background(bg_color)

    render_panels()

    canvas_border = 30
    draw_canvas_border(canvas_border, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "line_move_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wm, hm)

