"""

GENUARY 2021 - Tree
Draw 3 trees

Jan10 2021

"""
w, h = 840, 840
margin = 20

NUM_LEAVES = 140  # also, points in the spiral
THETA_INC = 0.15
RADIUS_INC = 0.6
MIN_RADIUS = 10


def render_foliage(spiral_center):
    """ Draw the Spiral in reverse, from out to in """

    noStroke()

    scx, scy = spiral_center
    pushMatrix()
    translate(scx, scy)
    r = NUM_LEAVES * RADIUS_INC + MIN_RADIUS
    theta = NUM_LEAVES * THETA_INC
    for leaf in range(NUM_LEAVES):
        fill(0, 200, 0, 30 + leaf)  # 30

        if not leaf % 3:
            stroke(50)
        else:
            noStroke()

        x = r * cos(theta)
        y = r * sin(theta)

        ellipse(x, y, r, r)

        theta -= THETA_INC  # Decrement the angle
        r -= RADIUS_INC  # Decrement the radius
    popMatrix()


TREE_RINGS = 25


def render_trunk(spiral_center):
    """ Draw the Spiral in reverse, from out to in """

    noStroke()
    scx, scy = spiral_center
    pushMatrix()
    translate(scx, scy)
    y = 100
    for ring in range(TREE_RINGS):
        fill(139, 69, 19, 30 + ring * 4)  # 30
        y += 5
        if not ring % 3:
            stroke(50)
        else:
            noStroke()

        ellipse(0, y, 40, 20)

    popMatrix()


def setup():
    size(w, h)
    background(201)

    for tnum in range(3):
        sc = (width * (tnum + 1) / 4, height / 2)
        render_foliage(sc)
        render_trunk(sc)

    draw_canvas_border(20, border_color=200)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    titlestr = "ev_"
    save("images/" + titlestr + coda + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

