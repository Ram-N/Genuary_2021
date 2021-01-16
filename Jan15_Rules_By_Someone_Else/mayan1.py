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
    "#013220",
    "#024b30",
    "#036440",
    "#037d50",
    "#049660",
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


def setup():
    size(wm, hm)
    render_background()

    fill(255)
    for yi in range(num_rows):
        for xi in range(num_cols):
            y, x = 2 * margin + (margin + ts) * xi, 2 * margin + (margin + ts) * yi
            fill(33, 150)
            rect(x + drop, y + drop, ts, ts)
            fill(155)
            if (xi, yi) in color_d:
                fill(palette[color_d[(xi, yi)]])
            rect(x, y, ts, ts)

    draw_canvas_border(margin, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "mayan1_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, wm, hm)

