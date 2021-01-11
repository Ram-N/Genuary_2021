"""

GENUARY 2021 - Interference patterns

This sketch moves a set of particles at velocities corresponding to a
vector field generated via the perlin noise

Jan09 2021

"""
w, h = 840, 840

scale = 0.008  # scale of the noise
step_size = 20  # how fast the particles move
offset = 100  # offset in the noise input to get a different x & y velocities

rows = 80
cols = 80
margin = 20

ystep = (h - 2 * margin) / (rows - 1)
xstep = (w - 2 * margin) / (cols - 1)

bidirection = 0.5

EPSILON = 3
INTERFERENCE = 50
STARTX, ENDX, STARTY, ENDY = 0.3, 0.7, 0.4, 0.5

xstart = margin  # (w - (cols - 1) * xstep) / 2
ystart = margin  # (h - (rows - 1) * ystep) / 2

particles = []


def out_of_bounds(p):
    if p.x <= xstart or p.x > w - xstart:
        return 1
    if p.y <= ystart or p.y > h - ystart:
        return 1
    return 0


def in_interference_zone(x, y):

    if (
        (x >= STARTX * width)
        and (x <= ENDX * width)
        and (y >= STARTY * height)
        and (y <= ENDY * height)
    ):
        return 1
    return 0


def update_path(particles):

    strokeWeight(3)

    for p in particles:
        stroke(max(100, (10 * p.row) % 255), 0, 0)
        # stroke((50 + 10 * p.row) % 255, p.id % 255, (50 + 10 * p.column) % 255)
        # stroke((50 + 10 * p.row) % 255, p.id % 255, max((255 - p.id) % 255, 0))
        # stroke(50, 150, 100)
        strokeWeight(1)
        if p.active:
            x, y = p.x, p.y  # current position
            x_perturb = noise(scale * x, scale * y) - bidirection
            y_perturb = noise(offset + scale * x, offset + scale * y) - bidirection
            dx = step_size * x_perturb
            dy = step_size * y_perturb

            # if new loc is within Interference box, go along the edges...
            if in_interference_zone(p.x + dx, p.y + dy):
                # new loc should be along the walls
                # one of dx or dy has to be zero, the other can stay as it is
                if abs(p.y + dy - (height * STARTY)) < EPSILON:
                    # print(p.id, p.x, p.y)
                    dy = 0
                if abs(p.y + dy - (height * ENDY)) < EPSILON:
                    # print(p.id, p.x, p.y)
                    dy = 0
                if abs(p.x + dx - (width * STARTX)) < EPSILON:
                    # print(p.id, p.x, p.y, width * STARTX)
                    dy = 0
                if abs(p.x + dx - (width * ENDX)) < EPSILON:
                    # print(p.id, p.x, p.y)
                    dy = 0

            # Store its new location
            p.x += dx
            p.y += dy

            if out_of_bounds(p):
                p.active = False
            else:  # draw a tiny line from prev position to updated position
                if not in_interference_zone(p.x, p.y):
                    line(x, y, p.x, p.y)


def setup():
    size(w, h)
    background(201)

    # stroke(211)
    # fill(211)
    # rect(STARTX * w, STARTY * h, (ENDX - STARTX) * w, (ENDY - STARTY) * h)
    # noFill()

    for row in range(rows):
        for col in range(cols):
            xPos = xstart + xstep * col  # starting xposition
            yPos = ystart + ystep * row  # starting yposition
            if not in_interference_zone(xPos, yPos):
                p = PVector(xPos, yPos)
                p.row, p.column = row, col
                particles.append(p)

    i = 0
    for p in particles:
        p.active = True
        p.id = i
        p.ix, p.iy = p.x, p.y  # initial positions
        i += 1

    for i in range(800):
        update_path(particles)

    draw_canvas_border(20, border_color=200)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    titlestr = "interference_"
    save("images/" + titlestr + coda + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

