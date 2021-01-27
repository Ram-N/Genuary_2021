"""
GENUARY 2021 - "2D Perspective"

Ram Narasimhan
Jan26 2021
"""

from datetime import datetime

bg_color = 20


def setup():
    background(bg_color)
    size(1000, 1000, P3D)

    strokeWeight(3)
    lights()

    fov = PI / 3.0
    cameraZ = (height / 2.0) / tan(fov / 2.0)
    perspective(fov, float(width) / float(height), cameraZ / 2.0, cameraZ * 2.0)

    num_pts = 12
    a_step = TWO_PI / num_pts
    rots = [
        10 * a_step,
        10 * a_step,
        9.5 * a_step,
        9 * a_step,
        8.5 * a_step,
        8 * a_step,
        8 * a_step,
        8 * a_step,
        8 * a_step,
        9 * a_step,
        10 * a_step,
        10 * a_step,
    ]

    fill(108, 187, 60, 120)  # green
    fill(255, 216, 1, 120)  # yellow
    fill(181, 101, 30, 120)  # brown
    radius = 450
    for c in range(num_pts):
        theta = c * a_step
        x = radius * cos(theta)
        y = radius * sin(theta)
        pushMatrix()
        translate(width / 2 + x, height / 2 + y)
        rotateY(rots[c])  # around the vertical Y axis
        box(300, 120, 120)
        popMatrix()

    radius = 300

    fill(250, 170, 160, 180)
    for c in range(num_pts):
        theta = c * a_step
        x = radius * cos(theta)
        y = radius * sin(theta)
        pushMatrix()
        translate(width / 2 + x, height / 2 + y)
        rotateY(rots[c])  # around the vertical Y axis
        box(200, 80, 80)
        popMatrix()

    radius = 200
    fill(254, 64, 25, 200)
    for c in range(num_pts):
        theta = c * a_step
        x = radius * cos(theta)
        y = radius * sin(theta)
        pushMatrix()
        translate(width / 2 + x, height / 2 + y)
        rotateY(rots[c])  # around the vertical Y axis
        box(100, 40, 40)
        popMatrix()

    radius = 130
    fill(254, 195, 11, 240)
    for c in range(num_pts):
        theta = c * a_step
        x = radius * cos(theta)
        y = radius * sin(theta)
        pushMatrix()
        translate(width / 2 + x, height / 2 + y)
        rotateY(rots[c])  # around the vertical Y axis
        box(80, 30, 30)
        popMatrix()

    fill(220, 200, 240)
    ellipse(width / 2, height / 2, 50, 50)

    draw_canvas_border(40, border_color=120)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "boxes_"

    save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, 990, 990)

