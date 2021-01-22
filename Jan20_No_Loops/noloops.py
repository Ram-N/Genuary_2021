"""
GENUARY 2021 - "No Loops"

Ram Narasimhan
Jan20 2021

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


bg_color = 20

angle_step = TWO_PI / 60.0  # 6 degrees, in radians


def setup():
    size(wc, hc)
    background(bg_color)
    noFill()

    padding = 10  # gap between canvas margin and rendering form start

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

    #    strokeWeight(padding * 2)
    noStroke()
    fill(color_p[5])
    rect(canvas_margin / 2, canvas_margin / 2, wc - canvas_margin, hc - canvas_margin)

    fill(color_p[6])
    beginShape()
    vertex(canvas_margin / 2, canvas_margin / 2)
    vertex(width, 0)
    vertex(width, 229)
    vertex(201, 602)
    vertex(0, height)
    endShape(CLOSE)

    fill(color_p[4])
    beginShape()
    vertex(canvas_margin / 2, canvas_margin / 2)
    vertex(width, 0)
    vertex(width, 88)
    vertex(280, 360)
    vertex(0, 435)
    endShape(CLOSE)

    fill(color_p[1])
    beginShape()
    vertex(canvas_margin / 2, canvas_margin / 2)
    vertex(200, 0)
    vertex(80, 160)
    vertex(0, 200)
    endShape(CLOSE)

    strokeWeight(10)
    arc(width - 300, height, 500, 300, PI, 1.25 * PI, PIE)

    maroon = color_p[1]
    color_p = [
        "#fec5bb",
        "#fcd5ce",
        "#fae1dd",
        "#f8edeb",
        "#e8e8e4",
        "#d8e2dc",
        "#ece4db",
        "#ffe5d9",
        "#ffd7ba",
        "#fec89a",
    ]  # melon-cantaloupe, courtesy Coolors

    # 4-clover
    rw, rh = 155, 155
    cur = 100
    yh = 620
    fill(color_p[1])
    rect(yh - rw, yh - rh, rw, rh, cur, cur, 0, cur)
    rect(yh + 30, yh - rh, rw, rh, cur, cur, cur, 0)

    rect(yh + 30, yh + 30, rw, rh, 0, cur, cur, cur)
    # fill(252, 213, 206, 100)
    rect(yh - rw, yh + 30, rw, rh, cur, 0, cur, cur)

    # Trishul
    strokeWeight(10)
    ty = 300  # trishul y
    noFill()

    stroke(color_p[1])
    r = 40
    ellipse(500, ty, 40 + r, 40 + r)  # end rings
    ellipse(400, ty - 160, 30 + r, 30 + r)
    ellipse(450, ty - 101, 40 + r, 40 + r)

    strokeWeight(20)
    stroke("#001000")
    noFill()
    bezier(500, ty, 345, 342, 87, 89, 400, ty - 160)
    line(200, ty, 450, ty - 101)
    # bezier(300, 200, 345, 342, 87, 89, 200, 140)

    stroke("#001000")
    ellipse(500, ty, 40, 40)  # end caps
    ellipse(400, ty - 160, 30, 30)
    ellipse(450, ty - 101, 40, 40)

    ellipse(200, ty, 30, 30)  # base endcap

    # base dots
    tex = 130
    stroke("#f5d2d3")  # brown
    # stroke("#264653")
    ellipse(tex, ty + 20, 10, 10)
    ellipse(tex + 20, ty - 30, 10, 10)
    ellipse(tex + 60, ty - 60, 10, 10)
    ellipse(tex + 40, ty + 60, 10, 10)
    ellipse(tex + 105, ty + 55, 10, 10)

    # candelabra
    tx, ty = 700, 100
    tw, th = 140, 40
    fill(maroon)
    stroke(maroon)
    triangle(tx, ty, tx + tw, ty - th, tx + tw, ty + th)
    triangle(tx, ty - th, tx, ty + th, tx + tw, ty)
    ty += 200
    triangle(tx, ty, tx + tw, ty - th, tx + tw, ty + th)
    triangle(tx, ty - th, tx, ty + th, tx + tw, ty)

    # Organ pipes
    stroke("#001000")
    ox, oy = 100, 500
    oh = 250
    xsp, ysp = 50, 32
    line(ox, oy, ox, oy + oh)
    oh -= ysp
    ox += xsp
    line(ox, oy, ox, oy + oh)
    oh -= ysp
    ox += xsp
    line(ox, oy, ox, oy + oh)
    oh -= ysp
    ox += xsp
    line(ox, oy, ox, oy + oh)
    oh -= ysp
    ox += xsp
    line(ox, oy, ox, oy + oh)

    print(canvas_margin)
    draw_canvas_border(canvas_margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "noloops_"
    save("images/" + titlestr + timestamp + ".png")

