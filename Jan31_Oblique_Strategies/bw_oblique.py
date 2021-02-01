"""
GENUARY 2021 - "Brian Eno's Oblique Strategies"

Ram Narasimhan
Jan31 2021

"""

from datetime import datetime
from shapes import nested_L, nested_squares

margin = 20
w, h, = 1040, 1040  # working area
wm, hm = w + 2 * margin, h + 2 * margin  # total size


color_p = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]


multigrid = {
    (0, 2): (2, 2),
    (1, 4): (2, 1),
    (3, 0): (2, 1),
    (4, 3): (1, 2),
    (3, 1): (1, 1),
}

# these squares should NOT be rendered. They are taken
anchor = (3, 1)
skip = [(0, 3), (1, 2), (1, 3), (2, 4), (4, 0), (4, 4)]


def render_panels():

    num_cols = 5
    num_rows = 5
    inter_cell = 20  # internal gap between 2 cells
    cell_margin = 20  # initial gutter between canvas margin
    # and the start of the first cell

    cw = (w - 2 * cell_margin - (num_cols - 1) * inter_cell) / (num_cols)
    ch = (h - 2 * cell_margin - (num_rows - 1) * inter_cell) / (num_rows)

    print(w, h, cw, ch)

    fill(bg_color + 20)
    noStroke()
    for yi in range(num_rows):
        for xi in range(num_cols):
            if (xi, yi) not in skip:
                if (xi, yi) in multigrid:  # these have to be treated differently
                    w_span = multigrid[(xi, yi)][0]
                    h_span = multigrid[(xi, yi)][1]
                    spl_w = cw * w_span + inter_cell * (w_span - 1)
                    spl_h = ch * h_span + inter_cell * (h_span - 1)
                    print(xi, yi, spl_w, spl_h)
                    orient = 0 if random(1) < 0.5 else 2
                else:  # regular 1x1 square
                    spl_w, spl_h = cw, ch
                    orient = int(random(4))

                x, y = (
                    margin + cell_margin + (inter_cell + cw) * xi,
                    margin + cell_margin + (inter_cell + ch) * yi,
                )
                print(xi, yi, x, y, "nw")
                cx, cy = x + spl_w / 2, y + spl_h / 2
                rect(x, y, spl_w, spl_h)  # cell outer rect
                # print(xi, yi, "spl", spl_w, spl_h, x, y, "nw", cx, cy, "cw")

                if (xi, yi) == anchor:
                    nested_squares(cx, cy, spl_w, spl_h, 10, orient)
                else:
                    nested_L(cx, cy, spl_w, spl_h, 10, orient)


bg_color = 20


def setup():
    size(wm, hm)
    background(bg_color)

    render_panels()

    canvas_border = 30
    draw_canvas_border(canvas_border, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "oblique_"
    save("frames/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wm, hm)
