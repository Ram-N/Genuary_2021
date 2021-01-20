"""
GENUARY 2021 - "Increasing randomness along the y-axis"

Ram Narasimhan
Jan19 2021

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


bg_color = 20

# Try changing any of these PARAMETERS
FREQ = [0.5, 1, 2]
AMPLITUDE = [20, 50, 80]
ERASE_TRAILS = False  # True or False are valid options
angle_step = TWO_PI / 60.0  # 6 degrees, in radians


def setup():
    size(wc, hc)
    background(bg_color)

    padding = 9  # gap between canvas margin and rendering form start
    ystep = 27
    xstep = 5
    stroke(200)
    strokeWeight(2)
    num_waves = 1 + (hc - 2 * (padding + canvas_margin)) / ystep

    zones = [x for x in range(num_waves) if not x % 5]

    print(num_waves, "waves")
    print("yzones", zones)
    print(num_waves, padding, h, hc, ystep)

    num_randomness_step = 6  # bands of increasing randomness.
    min_amplitude = 10  # beyond this, the amp goes up in monotonically with y
    # for y in range(num_waves):
    #     print(sw, num_waves, y)

    start = canvas_margin + padding
    for y in range(num_waves):
        ybase = ystep * y + start
        amp = max(num_waves - y, min_amplitude)
        sw = 2 + (num_waves - y) // 10  # strokWeigth goes up in steps
        strokeWeight(sw)
        px, py = start, ybase + sin(angle_step * start) * amp
        for x in range(start, wc - start, xstep):
            rnd_base = num_waves // num_randomness_step - (
                y // num_randomness_step
            )  # starts from 4 and goes to 0 in bands
            yrand = random(rnd_base * 3)
            if x == start:
                yrand = 0
            yvert = sin(angle_step * x) * amp  # amplitude
            ypos = ybase + yvert + yrand

            # break up wave if y< zones[4], else print them all
            if y < zones[4]:
                if x % 2:
                    if y < zones[1] and random(1) < 0.5:
                        ellipse(x, ypos, 2, 2)
                    else:
                        line(px, py, x, ypos)
            else:
                line(px, py, x, ypos)
            px, py = x, ypos

    strokeWeight(padding * 2)
    noFill()
    stroke(bg_color)
    rect(canvas_margin / 2, canvas_margin / 2, wc - canvas_margin, hc - canvas_margin)

    print(canvas_margin)
    draw_canvas_border(canvas_margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "yrandom_"
    save("images/" + titlestr + timestamp + ".png")

