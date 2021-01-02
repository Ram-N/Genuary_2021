"""
Created as a sketch for Genuary 2021: https://genuary2021.github.io/prompts
Genuary 2021: Jan 02 Sketch

Rule 30

Author: Ram Narasimhan
"""

from grid import Grid

w, h = 840, 840
margin = 20
vector_length = 100
str_length = 30
# Ruleset is 30
# gen is a string of 0/1 of length L
start_gen = ["0"] * str_length + ["1"] + ["0"] * str_length
# print(start_gen)
NUM_GENERATIONS = 2 * str_length + 1


d30 = {
    "111": "0",
    "110": "0",
    "101": "0",
    "100": "1",
    "011": "1",
    "010": "1",
    "001": "1",
    "000": "0",
}


def get_next_gen(gen):
    """given a gen and a ruleset, produce the next gen."""

    # for now I have hardcoded Ruleset 30, via a d30 dictionary

    next_gen = []
    for d in range(0, len(gen) - 1):
        triplet = "".join([gen[d - 1], gen[d], gen[d + 1]])
        next_gen.append(d30[triplet])

    triplet = "".join([gen[-2], gen[-1], gen[0]])
    next_gen.append(d30[triplet])
    return next_gen


def draw_canvas_border():
    strokeWeight(margin)
    noFill()
    stroke(255)
    rect(0, 0, w, h)


def setup():
    size(w, h)
    background(100)

    gens = []
    gen = start_gen
    gens.append(gen)
    for g in range(NUM_GENERATIONS - 1):
        ng = get_next_gen(gen)
        gens.append(ng)
        gen = ng

    grid = Grid(NUM_GENERATIONS, len(start_gen), w, h, margin, margin)
    grid.render_cell_borders()

    for row in range(NUM_GENERATIONS):
        for col in range(len(start_gen)):
            cell = grid.get_cell(row, col)
            # print(cell.row, cell.col, row, col)
            if gens[row][col] == "1":
                cell.fill_cell()

    draw_canvas_border()
    coda = str(int(random(10000)))
    save("images/rule_30_" + coda + ".png")
