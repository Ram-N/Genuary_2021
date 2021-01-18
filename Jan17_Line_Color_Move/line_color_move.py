"""
GENUARY 2021 - "Draw A line, pick a color, move a bit"

Ram Narasimhan
Jan17 2021

"""

from datetime import datetime
from rn_utils import pick_one

canvas_margin = 30
w, h, = 880, 880  # working area
wm, hm = w + 2 * canvas_margin, h + 2 * canvas_margin  # total size


# Panels
panel_cols = 6
panel_rows = 6

inter_cell = 10  # internal gap between 2 panels
cell_margin = 10  # initial gutter between canvas margin & the start of the first panel

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
            fill(10)
            rect(x, y, pw, ph)
            draw_lines(x, y, pw, ph)  # inside panel
            print(x, y)


color_p = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
color_p = [
    #    "#264653",
    "#2a9d8f",
    "#e9c46a",
    "#f4a261",
    "#e76f51",
]  # courtesy Coolors

color_p = [
    "#7400b8",
    "#6930c3",
    "#5e60ce",
    "#5390d9",
    "#4ea8de",
    "#48bfe3",
    "#56cfe1",
    "#64dfdf",
    "#72efdd",
    "#80ffdb",
]  # purple-cyan, courtesy Coolors

color_p = [
    "#fec5bb",
    "#fcd5ce",
    "#fae1dd",
    "#f8edeb",
    "#e8e8e4",
    "#d8e2dc",
    "#ece4db",
    "#ffe5d9",
    "#ffd7ba",
    "#fec89a",
]  # melon-cantaloupe, courtesy Coolors

color_p = [
    #    "#03071e",
    #    "#370617",
    "#6a040f",
    "#9d0208",
    "#d00000",
    "#dc2f02",
    "#e85d04",
    "#f48c06",
    "#faa307",
    "#ffba08",
]  # brown-orange-red, courtesy Coolors


def draw_lines_given_direction(wx, wy, panel_width, panel_height, orient=0):

    strokeWeight(3)

    if orient == 0:
        y, ystep = 0, 5
        col = 0
        x = random(panel_width)
        lw_start = random(panel_width)
        while not y > panel_height:
            stroke(color_p[col % len(color_p)])
            # stroke(color_p[int(random(len(color_p)))])

            lw = (lw_start + (col * 3)) % panel_width
            if x + lw > panel_width:
                line(min(x, panel_width), y, panel_width, y)
                line(0, y, min(x + lw - panel_width, panel_width), y)
                x = x + lw - panel_width
            else:
                line(x, y, x + lw, y)
                x = x + lw
            y += ystep
            col += 1
    else:
        x, xstep = 0, 5
        col = 0
        y = random(panel_height)
        lh_start = random(panel_height)
        while not x > panel_width:
            stroke(color_p[col % len(color_p)])
            # stroke(color_p[int(random(len(color_p)))])

            lh = (lh_start + (col * 3)) % panel_height
            if y + lh > panel_height:
                line(x, min(x, panel_width), x, panel_height)
                line(x, 0, x, min(y + lh - panel_height, panel_height))
                y = y + lh - panel_height
            else:
                line(x, y, x, y + lh)
                y = y + lh
            x += xstep
            col += 1


def draw_lines(wx, wy, panel_width, panel_height):
    pushStyle()
    fill(200)
    pushMatrix()
    translate(wx, wy)
    orient = 1 if not (wx + wy) % 2 else 0
    draw_lines_given_direction(wx, wy, panel_width, panel_height, orient)
    popMatrix()
    popStyle()


bg_color = 20


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

