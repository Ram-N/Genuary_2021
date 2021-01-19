"""
GENUARY 2021 - "One Process Grows, Another Prunes"

Ram Narasimhan
Jan18 2021

"""

from datetime import datetime
from force_field import render_particles_in_grid, render_xy_particle


canvas_margin = 30
w, h, = 800, 800  # working area
wc, hc = w + 2 * canvas_margin, h + 2 * canvas_margin  # total canvas dimensions


def draw_canvas_border(canvas_margin, border_color=255):
    """Draws a rectangular border of width canvas_margin that frames the canvas"""
    strokeWeight(canvas_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wc, hc)


color_p = [
    #    "#03071e",
    #    "#370617",
    "#6a040f",
    "#9d0208",
    "#d00000",
    "#dc2f02",
    "#e85d04",
    "#f48c06",
    "#faa307",
    "#ffba08",
]  # brown-orange-red, courtesy Coolors


def shoot_darts(x, y, theta, num_darts, next_ring):

    targets = []
    r = next_ring
    for dart in range(num_darts):
        rnd_angle = theta + random(-0.25, 0.25)
        tx, ty = r * cos(rnd_angle), r * sin(rnd_angle)
        line(x, y, tx, ty)

        # Prune and return the new points...tx, ty
        if random(1) < 0.1:
            targets.append((tx, ty))


bg_color = 20


def setup():
    size(wc, hc)
    background(bg_color)

    pushMatrix()
    translate(width / 2, height / 2)
    num_points = 10
    r = 100
    stroke(200)
    for s in range(num_points):
        angle_step = TWO_PI / num_points
        theta = s * angle_step
        x, y = r * cos(theta), r * sin(theta)
        # shoot 10 more darts
        new_targets = shoot_darts(x, y, theta, 10, r + 100)

    popMatrix()

    draw_canvas_border(canvas_margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "grow_prune_"
    save("images/" + titlestr + timestamp + ".png")

