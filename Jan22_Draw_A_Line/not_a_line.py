"""
GENUARY 2021 - "Draw a Line. Wrong Answers only"

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

    midcolor = 180

    fill(midcolor)
    rect(width / 2, 0, width / 2, height / 2)  # top right
    rect(0, height / 2, width / 2, height / 2)  # bottom left

    stroke(125)
    fill(125)
    strokeWeight(2)
    num_lines = 80
    ystart = 50
    xstart = 50
    ystep, dstep = 10, 10
    for l in range(200):
        for d in range(3, ystart + l * ystep, dstep):
            ellipse(d, ystart + l * ystep - d, 4, 4)

    #        line(0, ystart + l * ystep, ystart + l * ystep, 0)

    w8 = width / 8
    h9 = height / 9
    w2 = width / 2
    h2 = height / 2

    strokeWeight(40)

    # rope
    noFill()
    stroke(bg_color)
    bezier(2.1 * w8, 0, 2.5 * w8, 0.3 * h9, 3 * w8, 1.3 * h9, w2, h9)  # top
    stroke(midcolor)
    bezier(w2, h9, 9 * w8, 1.3 * h9, 8 * w8, 1.6 * h9, w2, 2 * h9)

    adj = 13
    bezier(
        w2, 3 * h9, 8 * w8, 3.9 * h9, 7.5 * w8, 4 * h9, 6.48 * w8, h2 - adj
    )  # top rt 2nd

    stroke(bg_color)
    bezier(
        6.5 * w8, h2 + adj, 5.5 * w8, h2 + 170, 4.5 * w8, 6 * h9, w2 + 1, 6 * h9
    )  # low rt

    stroke(bg_color)
    bezier(
        w2, 2 * h9, 1 * w8, h9 + 1.3 * h9, 2 * w8, h9 + 1.6 * h9, w2, 3 * h9
    )  # top left arc

    stroke(midcolor)
    bezier(w2, 6 * h9, 1 * w8, 7 * h9, 2 * w8, 8 * h9, 2 * w8, 9 * h9)

    # patch up
    stroke(bg_color)
    strokeWeight(8)
    line(w2 + 3, 6 * h9 + 24, w2 + 3, 6 * h9 - 15)
    fill(bg_color)
    triangle(6.48 * w8 - 7, h2 + 3, 6.63 * w8, h2 + 3, 6.63 * w8, h2 + 20)

    stroke(midcolor)
    line(w2 + 3, 3 * h9 + 22, w2 + 3, 3 * h9 - 23)

    fill(midcolor)
    triangle(
        6.46 * w8 - 7, h2 - 3, 6.59 * w8, h2 - 3, 6.45 * w8, h2 - 20
    )  # upper rt tri

    draw_canvas_border(canvas_margin, border_color=midcolor)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "knot_"
    save("frames/" + titlestr + timestamp + ".png")

