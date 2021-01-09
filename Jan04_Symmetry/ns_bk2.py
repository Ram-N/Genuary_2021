"""
This sketch moves a set of particles at velocities corresponding to a
vector field generated via the perlin noise

Original Inspiration by: u/YttriumThoriumOxide/ (reddit)

"""
w, h = 800, 800

scale = 0.008  # scale of the noise
step_size = 80  # how fast the particles move
offset = 100  # offset in the noise input to get a different x & y velocities

rows = 25
cols = 30
ystep = 25
xstep = 25

bidirection = 0.5

xstart = (w - (cols - 1) * xstep) / 2
ystart = (h - (rows - 1) * ystep) / 2

particles = []


def out_of_bounds(p):
    if p.x <= xstart or p.x > w - xstart:
        return 1
    if p.y <= ystart or p.y > h - ystart:
        return 1
    return 0


def update_path(particles):

    strokeWeight(1)

    for p in particles:
        # stroke(50, min(max(p.id, 100), 220), 100)
        stroke(50, 150, 100)
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
            else:
                if p.symmetry:
                    stroke(0, 225, 50)  # change color
                    # strokeWeight(2)
                    for rot in range(ROT_AXIS):
                        pushMatrix()
                        translate(p.ix, p.iy)  # particle origin
                        # print(rot, x, y, p.x, p.y)
                        rotate(TWO_PI / ROT_AXIS * rot)
                        line(0, 0, dx * 2, dy * 2)
                        popMatrix()
                else:
                    # draw a tiny line from old position to new position
                    line(x, y, p.x, p.y)
                    # point(p.x, p.y)


ROT_AXIS = 4


def setup():
    size(w, h)
    background(51)

    for row in range(rows):
        for col in range(cols):
            xPos = xstart + xstep * col  # starting xposition
            yPos = ystart + ystep * row  # starting yposition
            particles.append(PVector(xPos, yPos))

    i = 0
    for p in particles:
        p.active = True
        p.id = i
        p.ix, p.iy = p.x, p.y  # initial positions
        p.symmetry = False
        # if random(1) < 0.01:
        #     p.symmetry = True
        i += 1

    symms = [173, 220, 440, 610]
    for p in particles:
        if p.id in symms:
            p.symmetry = True

    for i in range(750):
        update_path(particles)

    draw_canvas_border(20, border_color=200)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    titlestr = "noise_symm_"
    save("images/" + titlestr + coda + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)
