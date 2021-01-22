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


def sphinx(x, y, tw, th):
    # noStroke()
    beginShape()
    vertex(x, y)
    vertex(x + tw, y - 2 * th)
    vertex(x + 1.5 * tw, y - th)
    vertex(x + 2.5 * tw, y - th)
    vertex(x + 3 * tw, y)
    endShape(CLOSE)


tw, th = 14, 20


def draw_form2(x, call_num, transx, transy):
    pushMatrix()
    translate(transx, transy)

    if transy == lift + height / 2:
        rotate(PI)  # / 3 * call_num)
    fill(purp[call_num % len(purp)])
    triangle(-x, x, 0, -x, x, x)
    popMatrix()


def draw_lines(x, call_num, transx, transy):
    pushMatrix()
    translate(transx, transy)

    # if transy == 200 + height / 2:
    rotate(PI / 3 * call_num)
    strokeWeight(3)
    stroke(200 + call_num)
    line(80 + x, 0, 800 + x, x - 100)
    noStroke()
    popMatrix()


def draw_sphinx(x, call_num, transx, transy):
    pushMatrix()
    translate(transx, transy)

    flip = 1
    if transy == -1 * lift + height / 2:
        flip = 0
    rotate(PI / 8 * call_num + (PI * flip) + 0.7)
    fill(color_p[(call_num - 3) % len(color_p)])
    sphinx(100, 100, x, x)
    popMatrix()


lift = 250
shiftx = 200


def recursion_spx(x, call_num):

    if x < 5:
        return

    call_num += 1
    draw_sphinx(x, call_num, width / 2 - shiftx, lift + height / 2)
    draw_sphinx(x, call_num, width / 2 + shiftx, -1 * lift + height / 2)  # upper whorl

    recursion_spx(x / 4, call_num)
    recursion_spx(x / 2, call_num)
    recursion_spx(3 * x / 4, call_num)


def recursion(x, call_num):

    if x < 10:
        return

    call_num += 1

    draw_form2(x, call_num, width / 2 + shiftx, -lift + height / 2)  # upper whorl
    draw_form2(x, call_num, width / 2 - shiftx, lift + height / 2)

    #    draw_lines(x, call_num, width / 2 - shiftx, lift + height / 2)

    recursion(x / 4, call_num)
    recursion(x / 2, call_num)
    recursion(3 * x / 4, call_num)


call_num = 0  # variable to keep track of recursion count
# used for coloring


def setup():
    global call_num

    size(wc, hc)
    background(bg_color)
    noFill()
    padding = 10  # gap between canvas margin and rendering form start

    fill(125)
    triangle(0, 0, 0, height, width, height)
    rect(width / 2, 0, width / 2, height / 2)

    fill(bg_color)
    rect(0, height / 2, width / 2, height / 2)

    fill(color_p[3])

    recursion_spx(150, call_num)  # sphinxes
    call_num = 0
    recursion(80, call_num)

    draw_canvas_border(canvas_margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "recur_"
    save("frames/" + titlestr + timestamp + ".png")

