"""
GENUARY 2021 - "Someone Else's Rules"
On a Background of flow field, lay out colored tiles per Alfred Jensen's square.

Ram Narasimhan
Jan15 2021

"""

from datetime import datetime

margin = 30
w, h, = 910, 910
wm, hm = w + 2 * margin, h + 2 * margin

# pastels
# "#cdb8bc",
# "#b89aa0",
# "#ad8b92",
# "#a37c84",
# "#986d76",


reds = [
    "#de5606",
    "#f9381e",
    "#f72407",
    "#de2006",
    "#ac1905",
    "#955d04",
    "#ad6d05",
    "#df8c06",
    "#f89c07",
    "#fab038",
    # "#b12060",
    # "#d11f0b",
    # "#fd2c3b",
    # "#fddbd0",
    # "#a93705",
    # "#c7908d",
    # "#df6a92",
    # "#7d5547",
    # "#f97930",
    # "#f82387",
]

greens = [
    # "#58b5e1",
    # "#8cd3ff",
    # "#1aa7ee",
    # "#26ABED",
    # "#0d2cf7f",
    "#3ac2f9",
    "#08b3f8",
    "#06a2e1",
    "#0590c8",
    "#046c96",
    "#036440",
    "#037d50",
    "#049660",
    "#37c12",
    "#049515",
]

palette = [
    "#36225E",  # dark blue
    "#FE4019",  # orange
    "#e71d36",  # red
    "#0B85CF",  # light blue
    "#FF5FB9",  # pink
    "#2ec4b6",  # teal
    "#f69e55",  # orange
    "#FFA900",  # yellow
    "#ffffff",  # white
]

# interleave the two lists...
palette = [val for pair in zip(reds, greens) for val in pair] + ["#989898"]


def render_background():
    ystep = 20
    num = height / ystep
    noStroke()
    for ry in range(int(num)):
        fill(ry, 31, 49, 150 - ry)
        rect(0, ry * ystep, width, ystep)


bg_color = 250

ts = 50
num_cols = 11
num_rows = 11
drop = 10

color_d = {
    (0, 0): 18,
    (1, 1): 16,
    (2, 2): 14,
    (3, 3): 12,
    (4, 4): 10,
    (5, 5): 20,
    (6, 6): 11,
    (7, 7): 13,
    (8, 8): 15,
    (9, 9): 17,
    (10, 10): 19,
    (0, 4): 18,
    (0, 6): 0,
    (0, 10): 0,
    (1, 3): 16,
    (1, 7): 2,
    (1, 9): 2,
    (2, 8): 4,
    (3, 1): 12,
    (3, 7): 6,
    (3, 9): 6,
    (4, 0): 10,
    (4, 6): 8,
    (4, 10): 8,
    (6, 0): 9,
    (6, 4): 9,
    (6, 10): 11,
    (7, 1): 7,
    (7, 3): 7,
    (7, 9): 13,
    (8, 2): 5,
    (9, 1): 3,
    (9, 3): 3,
    (9, 7): 17,
    (10, 0): 1,
    (10, 4): 1,
    (10, 6): 19,
}


def render_mayan_postits():
    noStroke()
    for yi in range(num_rows):
        for xi in range(num_cols):
            y, x = 2 * margin + (margin + ts) * xi, 2 * margin + (margin + ts) * yi
            fill(21, 4, 149, 150)
            rect(x + drop, y + drop, ts, ts)
            fill(155, 200)
            if (xi, yi) in color_d:
                fill(palette[color_d[(xi, yi)]])
            rect(x, y, ts, ts)


def update_path(particles):

    strokeWeight(1)

    for p in particles:
        cnum = max(160, (10 * p.row) % 255)
        stroke(cnum)
        # stroke((10 * p.row) % 255, (10 * p.row) % 255, (10 * p.row) % 255)
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

            # p gets displaced slightly. Store its new location
            p.x += dx
            p.y += dy

            if out_of_bounds(p):
                p.active = False
            else:  # draw a tiny line from prev position to updated position
                line(x, y, p.x, p.y)


def out_of_bounds(p):
    if p.x <= margin or p.x > wm - margin:
        return 1
    if p.y <= margin or p.y > hm - margin:
        return 1
    return 0


scale = 0.008  # scale of the noise
step_size = 20  # how fast the particles move
offset = 100  # offset in the noise input to get a different x & y velocities

rows = 20
cols = 20

ystep = (hm - 2 * margin) / (rows - 1)
xstep = (wm - 2 * margin) / (cols - 1)

bidirection = 0  # 0.5
xstart = margin  # (w - (cols - 1) * xstep) / 2
ystart = margin  # (h - (rows - 1) * ystep) / 2

particles = []


def setup():
    size(wm, hm)
    background(20)
    #    render_background()

    for row in range(rows):
        for col in range(cols):
            xPos = xstart + xstep * col  # starting xposition
            yPos = ystart + ystep * row  # starting yposition
            p = PVector(xPos, yPos)
            p.row, p.column = row, col
            p.active = True
            p.id = row * num_cols + col
            particles.append(p)

    for i in range(800):
        update_path(particles)

    render_mayan_postits()

    draw_canvas_border(margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "mayan1_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wm, hm)

