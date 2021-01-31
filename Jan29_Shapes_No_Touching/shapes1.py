"""
GENUARY 2021 - "Any Shape, none can touch"

Ram Narasimhan
Jan29 2021

"""

from datetime import datetime
from shapes import circle_pack, hexagon

margin = 30
w, h, = 1020, 1020  # working area
wm, hm = w + 2 * margin, h + 2 * margin  # total size


color_p = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]


def blob(bx, by, bw, bh):
    """
    bw, bh = blob's desired width and height
    At the moment bh is being ignored...
    """

    pushMatrix()
    translate(bx, by)

    delta = bw * 0.1  # +-10% give

    rmin, rmax = bw - delta, bw + delta
    max_offset = 10
    num_sides = 30
    theta_increment = TWO_PI / num_sides

    beginShape()
    for a in range(num_sides):
        theta = a * theta_increment
        x_noise_offset = map(cos(theta), -1, 1, 0, max_offset)
        y_noise_offset = map(sin(theta), -1, 1, 0, max_offset)

        radius = map(noise(bx + x_noise_offset, by + y_noise_offset), 0, 1, rmin, rmax)
        x = radius * cos(theta)
        y = radius * sin(theta)
        vertex(x, y)
    endShape(CLOSE)

    popMatrix()


def render_blobs(circles):
    """
    given xy and r, generate noisy blob-like objects
    """
    for c in circles:
        cx, cy = c.x, c.y
        radius = c.radius

        shape_decision = random(1)

        red = map(c.x, 0, width, 40, 255)
        green = map(c.y, 0, height, 80, 255)
        blue = random(50)
        # if cx + cy < 300:
        #     red += random(100)
        #     green += random(100)
        fill(red, green, blue)

        if shape_decision > 0.5:
            blob(c.x, c.y, c.radius, c.radius)
        else:
            rectMode(CENTER)
            pushMatrix()
            translate(c.x, c.y)
            rotate(random(TWO_PI))

            if shape_decision > 0.4:
                rect(0, 0, c.radius, 2 * c.radius)
            elif shape_decision > 0.3:
                ellipse(0, 0, radius * 1.8, radius * 0.9)
            elif shape_decision > 0.2:
                hexagon(0, 0, 0, radius * 0.9)
            else:
                di = c.radius * 0.8
                triangle(0, -di, di, di, -di, di)

            popMatrix()

    rectMode(CORNER)


def render_circles(circles):

    fill(random(255), random(255), random(255))
    for c in circles:
        ellipse(c.x, c.y, 2 * c.radius, 2 * c.radius)


num_cols = 1
num_rows = 1


def render_panels():

    inter_cell = 50  # internal gap between 2 cells
    cell_margin = (
        20
    )  # initial gutter between canvas margin and the start of the first cell

    cw = (w - 2 * cell_margin - (num_cols - 1) * inter_cell) / (num_cols)
    ch = (h - 2 * cell_margin - (num_rows - 1) * inter_cell) / (num_rows)

    print(w, h, cw, ch)

    fill(bg_color)
    noStroke()
    for yi in range(num_rows):
        for xi in range(num_cols):
            x, y = (
                margin + cell_margin + (inter_cell + cw) * xi,
                margin + cell_margin + (inter_cell + ch) * yi,
            )
            rect(x, y, cw, ch)
            min_radius, max_radius = 20, 60
            # from common util:shapes.py
            circles = circle_pack(x, y, cw, ch, min_radius, max_radius, min_gap=10)

            render_blobs(circles)


bg_color = 20


def setup():
    size(wm, hm)
    background(bg_color)

    render_panels()

    canvas_border = 30
    draw_canvas_border(canvas_border, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "shapes_"
    save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wm, hm)

