"""
GENUARY 2021 - "One Process Grows, Another Prunes"

Ram Narasimhan
Jan18 2021

"""

from datetime import datetime

canvas_margin = 30
w, h, = 800, 800  # working area
wc, hc = w + 2 * canvas_margin, h + 2 * canvas_margin  # total canvas dimensions


def draw_canvas_border(canvas_margin, border_color=255):
    """Draws a rectangular border of width canvas_margin that frames the canvas"""
    strokeWeight(canvas_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wc, hc)


color_p = ["#036440", "#037d50", "#049660", "#37c12", "#049515"]  # greens


def shoot_darts(x, y, theta, num_darts, next_ring):

    targets = []
    r = next_ring
    # scol = 220 if num_darts == GROWTH else 150
    # scol = "#037d50" if num_darts == GROWTH else "#cdb8bc"
    # stroke(scol)
    for dart in range(num_darts):
        rnd_angle = theta + random(-0.25, 0.25)
        tx, ty = r * cos(rnd_angle), r * sin(rnd_angle)
        # stroke(color_p[dart % len(color_p)])
        stroke(170 + dart * 8)
        line(x, y, tx, ty)

        # Prune and return the new points...tx, ty
        if num_darts == GROWTH:
            if random(1) < 0.11:
                targets.append((tx, ty, rnd_angle))
            # else:
            #     if random(1) < 0.3:
            #         ellipse(tx, ty, 3, 3)  # pruned
        else:
            targets.append((tx, ty, rnd_angle))

    return targets


bg_color = 20

GROWTH = 9  # number of darts from each point when in the growth phase
# in the prune phase, just one dart emanates.


def setup():
    size(wc, hc)
    background(bg_color)

    pushMatrix()
    translate(width / 2, height / 2)
    num_points = 10
    r_init = 25
    rstep = 50
    stroke(200)
    num_levels = 8
    targets = {}
    for lev in range(num_levels + 1):
        ndarts = GROWTH if lev % 2 else 1
        targets[lev] = [r_init + lev * rstep, ndarts, []]

    initial_pts = []
    for s in range(num_points):
        angle_step = TWO_PI / num_points
        theta = s * angle_step
        x, y = r_init * cos(theta), r_init * sin(theta)
        initial_pts.append((x, y, theta))

    # dictionary has level: radius, growth, active
    targets[0][2] = initial_pts

    for lev in range(num_levels):
        pts = targets[lev][2]
        if pts:
            level_targets = []
            for pt in pts:
                x, y, theta = pt
                num_darts = targets[lev][1]
                # pt_targets are the new targets for ONE point.
                pt_targets = shoot_darts(x, y, theta, num_darts, targets[lev][0])
                if pt_targets:
                    for new_pt in pt_targets:
                        level_targets.append(new_pt)

            targets[lev + 1][2] = level_targets

    popMatrix()

    draw_canvas_border(canvas_margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "grow_prune_"
    save("images/" + titlestr + timestamp + ".png")

