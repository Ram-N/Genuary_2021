"""
GENUARY 2021 - "Recursion"

Ram Narasimhan
Jan21 2021

"""

from datetime import datetime

canvas_margin = 30
w, h, = 800, 800  # working area
wc, hc = w + 2 * canvas_margin, h + 2 * canvas_margin  # total canvas dimensions


def draw_canvas_border(canvas_margin, border_color=255):
    """Draws a rectangular border of width canvas_margin that frames the canvas"""
    strokeWeight(canvas_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wc, hc)


bg_color = 20


color_p = [
    # "#03071e",
    # "#370617",
    # "#6a040f",
    # "#9d0208",
    "#d00000",
    "#dc2f02",
    "#e85d04",
    "#f48c06",
    "#faa307",
    "#ffba08",
]  # brown-orange-red, courtesy Coolors

purp = [
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


def setup():

    size(wc, hc)
    background(bg_color)
    noFill()
    strokeCap(SQUARE)
    padding = 10  # gap between canvas margin and rendering form start

    fill(125)
    rect(width / 2, 0, width / 2, height / 2)  # top right
    rect(0, height / 2, width / 2, height / 2)  # bottom left

    strokeWeight(2)
    stroke(200)
    num_lines = 80
    ystart = 50
    xstart = 50
    ystep = (height - 2 * ystart) / (num_lines - 1)
    for l in range(num_lines):
        line(xstart, ystart + l * ystep, width - xstart, ystart + l * ystep)

    w8 = width / 8
    h9 = height / 9
    w2 = width / 2
    h2 = height / 2

    strokeWeight(15)

    # rope
    noFill()
    stroke(bg_color)
    bezier(2.1 * w8, 0, 2.5 * w8, 0.3 * h9, 3 * w8, 1.3 * h9, w2, h9)  # top
    stroke(125)
    bezier(w2, h9, 9 * w8, 1.3 * h9, 8 * w8, 1.6 * h9, w2, 2 * h9)

    bezier(
        w2, 3 * h9, 8 * w8, 3.9 * h9, 7.5 * w8, 4 * h9, 6.5 * w8, h2 - 5
    )  # top rt 2nd

    stroke(bg_color)
    bezier(
        6.5 * w8, h2 + 5, 5.5 * w8, 5 * h9, 4.5 * w8, 6 * h9, w2 + 1, 6 * h9
    )  # low rt

    stroke(bg_color)
    bezier(
        w2, 2 * h9, 1 * w8, h9 + 1.3 * h9, 2 * w8, h9 + 1.6 * h9, w2, 3 * h9
    )  # top left arc
    stroke(125)
    bezier(w2, 6 * h9, 1 * w8, 7 * h9, 2 * w8, 8 * h9, 2 * w8, 9 * h9)

    draw_canvas_border(canvas_margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "knot_"
    save("frames/" + titlestr + timestamp + ".png")

