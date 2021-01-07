"""
Created for Genuary2021.
Jan 05 - Code Golf

Author: Ram Narasimhan
"""

w, r = 1000, 60


def setup():
    size(w, w)
    for _ in range(w):
        s, c = random(w), random(_)
        fill(c, c / 2, c / 4)
        flip = random(1)
        if flip > 0.97:
            line(w - s, 0, w - s, w - c)
        if flip > 0.8:
            ellipse(w - s, w - c - 20, r, r)

    draw_canvas_border(20)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    titlestr = "code_golf_"
    save("images/" + titlestr + coda + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, w)

