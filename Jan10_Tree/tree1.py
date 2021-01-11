"""

GENUARY 2021 - Tree
Draw 3 trees, each tree is created entirely from one shape (rectangle, ellipse, or triangle.)

Ram Narasimhan
Jan10 2021


"""
w, h = 840, 840
margin = 20

NUM_LEAVES = 140  # also, points in the spiral
THETA_INC = 0.15
RADIUS_INC = 0.6
MIN_RADIUS = 10
TREE_RINGS = 25

kind_dict = {0: "R", 1: "E", 2: "T"}


def render_foliage(spiral_center, kind="E"):
    """ Draw the Spiral in reverse, from out to in """

    noStroke()
    rectMode(CENTER)

    scx, scy = spiral_center
    pushMatrix()
    translate(scx, scy)
    r = NUM_LEAVES * RADIUS_INC + MIN_RADIUS
    r2 = r / 2
    r4 = r / 4
    fill(20, 140, 25, 200)
    ellipse(0, 0, 50, 50)

    theta = NUM_LEAVES * THETA_INC
    for leaf in range(NUM_LEAVES):
        fill(20, 140, 25, 30 + leaf // 2)

        if not leaf % 5:
            stroke(0, 71, 49)
        else:
            noStroke()

        x = r * cos(theta)
        y = r * sin(theta)

        if kind == "R":
            rect(x, y, r, r2)
        elif kind == "T":
            triangle(x, y - 40, x - r4, y + r4, x + r4, y + r4)
        else:
            ellipse(x, y, r, r)

        theta -= THETA_INC  # Decrement the angle
        r -= RADIUS_INC  # Decrement the radius
    popMatrix()
    rectMode(CORNER)


def render_trunk(spiral_center, kind="E"):
    """ Draw the Spiral in reverse, from out to in """

    noStroke()
    scx, scy = spiral_center
    pushMatrix()
    rectMode(CENTER)

    translate(scx, scy)
    y = 100
    for ring in range(TREE_RINGS):
        fill(139, 69, 19, 30 + ring * 4)  # 30
        y += 5
        if not ring % 3:
            stroke(126, 46, 31)
            # stroke("#654321")
        else:
            noStroke()

        if kind == "R":
            rect(0, y, 40, 20)
        elif kind == "T":
            triangle(0, y, -20, y + 20, 20, y + 20)
        else:
            ellipse(0, y, 40, 20)

    popMatrix()
    rectMode(CORNER)


def render_forest():
    ystep = 20
    num = height / ystep
    noStroke()
    for ry in range(int(num)):
        fill(ry * 2, 71, 49, 150 - ry)
        rect(0, ry * ystep, width, ystep)

    fill("#fffdd0")
    ellipse(100, 100, 50, 50)  # moon

    # textSize(14)
    # text("#Genuary2021, Jan-10th", width - 200, height - 25)


def setup():
    size(w, h)
    background(201)

    render_forest()  # background

    for tnum in range(3):
        sc = (width * (tnum + 1) / 4, height / 2)
        render_foliage(sc, kind=kind_dict[tnum])
        render_trunk(sc, kind=kind_dict[tnum])

    draw_canvas_border(20, border_color=220)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    titlestr = "ev_"
    save("images/" + titlestr + coda + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

