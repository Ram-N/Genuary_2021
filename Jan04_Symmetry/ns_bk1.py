"""
This sketch moves a set of particles at velocities corresponding to a
vector field generated via the perlin noise

CONTROLS:
R: Start over from beginning
T: Start over with a new seed
S: Save the current frame to a file
Q: Quit program

Original Content by: u/YttriumThoriumOxide/
# https://www.reddit.com/r/generative/comments/i9hxhq/treating_the_perlin_noise_as_a_vector_field/
JS Code: https://pastebin.com/MnxFQQWV

This is a port to Python by Ram Narasimhan, following the JS code.
Note that p.add doesn't seem to work in the Python implementation

"""
w, h = 800, 800

scale = 0.008  # scale of the noise
speed = 80  # how fast the particles move
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
        stroke(50, min(100, 200), 100)
        if p.active:
            if p.id == 400:
                # print(p.x, p.y)
                stroke(50, 200, 50)
                p.symmetry = True

            x, y = p.x, p.y  # current position
            x_perturb = noise(scale * x, scale * y) - bidirection
            y_perturb = noise(offset + scale * x, offset + scale * y) - bidirection
            dx = speed * x_perturb
            dy = speed * y_perturb

            # p gets displaced slightly. Store its new location
            p.x += dx
            p.y += dy

            if out_of_bounds(p):
                p.active = False
            else:
                # if symmetry needed
                if p.symmetry:
                    stroke(225)  # change color
                    strokeWeight(2)
                    for rot in range(ROT_AXIS):
                        pushMatrix()
                        translate(x, y)
                        print(rot, x, y, p.x, p.y)
                        rotate(TWO_PI / ROT_AXIS * rot)
                        line(0, 0, dx, dy)
                        popMatrix()
                else:
                    # draw a tiny line from old position to new position
                    line(x, y, p.x, p.y)
                    # point(p.x, p.y)


ROT_AXIS = 7


def setup():
    size(w, h)
    background(51)
    # colorMode(HSB, 360, 450, 100)

    for row in range(rows):
        for col in range(cols):
            xPos = xstart + xstep * col  # starting xposition
            yPos = ystart + ystep * row  # starting yposition
            particles.append(PVector(xPos, yPos))

    i = 0
    for p in particles:
        p.active = True
        p.id = i
        p.symmetry = False
        # if random(1) < 0.01:
        #     p.symmetry = True
        i += 1

    for i in range(15):
        update_path(particles)

