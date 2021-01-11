"""

GENUARY 2021 - Interference patterns

This sketch moves a set of particles at velocities corresponding to a
vector field generated via the perlin noise

Jan09 2021

"""
w, h = 800, 800

scale = 0.008  # scale of the noise
step_size = 20  # how fast the particles move
offset = 100  # offset in the noise input to get a different x & y velocities

rows = 50
cols = 50
margin = 20

ystep = (h - 2 * margin) / (rows - 1)
xstep = (w - 2 * margin) / (cols - 1)

bidirection = 0.5

INTERFERENCE = 50
STARTX, ENDX, STARTY, ENDY = 0.6, 1, 0.66, 0.73

xstart = margin  # (w - (cols - 1) * xstep) / 2
ystart = margin  # (h - (rows - 1) * ystep) / 2

particles = []


def out_of_bounds(p):
    if p.x <= xstart or p.x > w - xstart:
        return 1
    if p.y <= ystart or p.y > h - ystart:
        return 1
    return 0


def in_interference_zone(p):

    if (
        (p.x > STARTX * width)
        and (p.x < ENDX * width)
        and (p.y > STARTY * height)
        and (p.y < ENDY * height)
    ):
        return 1
    return 0


def update_path(particles):

    strokeWeight(1)

    for p in particles:
        stroke((50 + 10 * p.row) % 255, p.id % 255, (50 + 10 * p.column) % 255)
        # stroke((50 + 10 * p.row) % 255, p.id % 255, max((255 - p.id) % 255, 0))
        # stroke(50, 150, 100)
        strokeWeight(1)
        if p.active:
            x, y = p.x, p.y  # current position
            x_perturb = noise(scale * x, scale * y) - bidirection
            y_perturb = noise(offset + scale * x, offset + scale * y) - bidirection
            dx = step_size * x_perturb
            dy = step_size * y_perturb

            # p gets displaced slightly. Store its new location
            p.x += dx
            p.y += dy

            if out_of_bounds(p):
                p.active = False
            else:  # draw a tiny line from prev position to updated position
                if not in_interference_zone(p):
                    line(x, y, p.x, p.y)


def setup():
    size(w, h)
    background(51)

    for row in range(rows):
        for col in range(cols):
            xPos = xstart + xstep * col  # starting xposition
            yPos = ystart + ystep * row  # starting yposition
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

