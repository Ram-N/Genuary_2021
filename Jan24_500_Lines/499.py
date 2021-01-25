"""
GENUARY 2021 - "500 Lines"

Ram Narasimhan
Jan24 2021

"""

from datetime import datetime

margin = 0
w, h, = 960, 960  # working area of canvas
wm, hm = w + 2 * margin, h + 2 * margin


def render_background():
    ystep = 20
    num = height / ystep
    noStroke()
    for ry in range(int(num)):
        fill(ry, 31, 49, 150 - ry)
        rect(0, ry * ystep, width, ystep)


bg_color = 250


def generate_points(num_pts, range_x, range_y, xfree, yfree):
    """returns a set of xy coords"""

    xmin, xmax = range_x
    ymin, ymax = range_y
    pts = []

    xstep = (xmax - xmin) / (num_pts + 1)
    ystep = (ymax - ymin) / (num_pts + 1)

    for p in range(num_pts):
        x = xmin + xstep * p - xfree + int(random(xfree + 1))
        y = ymin + ystep * p - yfree + int(random(yfree + 1))
        pts.append((x, y))

    return pts


def connect_pair(pair, freedom_len, column="L"):
    xya, xyd = pair
    xa, ya = xya
    xd, yd = xyd

    flip = 1 if column == "L" else -1

    for e in range(NUM_ECHO):
        eps = e / (NUM_ECHO + 1.0)
        cw = freedom_len * eps * 2
        bez1x = xa + cw
        bez1y = ya + cw * flip
        bez2x = xd - cw
        bez2y = yd - cw * flip
        ystart = ya + 2 * e * flip
        yend = yd - 2 * e * flip
        bezier(xa, ystart, bez1x, bez1y, bez2x, bez2y, xd, yend)


def square_trail(x, y, dir="N"):
    pushMatrix()
    translate(x, y)
    rotate(PI / 4)
    rect(0, 0, 40, 40)
    popMatrix()

    flip = 1 if dir == "N" else -1

    xstart = 150
    ystart = 120
    xstep = (width / 2 - xstart) / 12
    ystep = (200 - ystart) / 12
    for sq in range(12):
        pushMatrix()
        translate(x + xstep * sq, y - ystep * sq * flip)
        rotate(PI / 4)
        rect(0, 0, 40, 40)
        popMatrix()

        pushMatrix()
        translate(x - xstep * sq, y - ystep * sq * flip)
        rotate(PI / 4)
        rect(0, 0, 40, 40)
        popMatrix()


NUM_ECHO = 10


def setup():
    size(wm, hm)  # including margin
    background(bg_color)
    stroke(40)
    noFill()

    strokeWeight(2)
    ypos = 100
    square_trail(width / 2, ypos, "N")
    square_trail(width / 2, height - 2.3 * ypos, "S")

    strokeWeight(1)

    num_pts = 15
    wxstart = 50
    span = width / 2 - wxstart - 20  # how long is each line?
    wxend = wxstart + 40

    axemax = width / 2 - 20
    axemin = axemax - 30
    westA = generate_points(num_pts, (wxstart, wxend), (83, 888), xfree=25, yfree=10)
    eastA = generate_points(num_pts, (axemax, axemax), (200, 750), xfree=0, yfree=10)

    # eastA = generate_points(
    #     num_pts, (80 + span, 80 + span), (200, 750), xfree=0, yfree=10
    # )

    print(eastA)

    # B is the right column

    bxwmin = width / 2 + 20
    bxwmax = bxwmin

    bxemax = width - wxstart
    bxemin = bxemax - 30

    westB = generate_points(num_pts, (bxwmin, bxwmax), (200, 750), xfree=0, yfree=10)
    eastB = generate_points(num_pts, (bxemin, bxemax), (83, 888), xfree=25, yfree=8)

    for pair in range(num_pts):
        exy, wxy = westA[pair], eastA[pair]
        connect_pair((exy, wxy), 50, "L")
        exy, wxy = westB[pair], eastB[pair]
        connect_pair((exy, wxy), 50, "R")

    draw_canvas_border(35, border_color=125)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "D500_"
    save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

