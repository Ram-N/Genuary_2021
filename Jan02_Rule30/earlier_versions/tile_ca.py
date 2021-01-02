"""
Created as a sketch for Genuary 2021: https://genuary2021.github.io/prompts
Genuary 2021: Jan 02 Sketch

Rule 30

Author: Ram Narasimhan
"""

from colors import COLORS, RED_COLORS, BLUE_COLORS
from grid import Grid

w, h = 1064, 1064
canvas_margin = 20
vector_length = 100
token_length = 30
# Ruleset is 30
# gen is a string of 0/1 of length L
start_gen = ["0"] * token_length + ["1"] + ["0"] * token_length
# print(start_gen)
NUM_GENERATIONS = 2 * token_length + 1

str_length = len(start_gen)  # number of 0/1 in the entire string
num_colors = len(COLORS)

TILE_WIDTH, TILE_HEIGHT = 256, 256

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


def draw_canvas_border(grid_margin):
    strokeWeight(grid_margin)
    noFill()
    stroke(255)
    rect(0, 0, w, h)


def render_single_tile(gens, grid, palette=COLORS):
    """

    grid is the Tile Grid
    """

    current_color_idx = 0
    num_colors = len(palette)
    for row in range(NUM_GENERATIONS):
        for col in range(str_length):
            cell = grid.get_cell(row, col)
            if gens[row][col] == "1":
                next_color_idx = (current_color_idx + 1) % num_colors
                cell.fill_cell(palette[next_color_idx])
                current_color_idx = next_color_idx


def create_tile(tile_nw_x, tile_nw_y, tile_colors, gens):

    tile_margin = 3
    tile_width, tile_height = TILE_WIDTH, TILE_HEIGHT
    # print("tile", tile_width, tile_height, tile_nw_x, tile_nw_y)
    tile_grid = Grid(
        NUM_GENERATIONS,
        str_length,
        tile_width,
        tile_height,
        tile_margin,
        tile_margin,
        tile_nw_x,
        tile_nw_y,
    )
    # tile_grid.render_grid_border()
    render_single_tile(gens, tile_grid, tile_colors)


def setup():
    size(w, h)
    background(225)

    gens = []
    gen = start_gen
    gens.append(gen)
    for g in range(NUM_GENERATIONS - 1):
        ng = get_next_gen(gen)
        gens.append(ng)
        gen = ng

    for tx in range(4):
        for ty in range(4):
            tile_nw_x, tile_nw_y = (
                canvas_margin + TILE_WIDTH * tx,
                canvas_margin + TILE_HEIGHT * ty,
            )
            tile_colors = BLUE_COLORS if tx % 2 else RED_COLORS
            # pushMatrix()
            # rotate(PI)
            create_tile(tile_nw_x, tile_nw_y, tile_colors, gens)
            # popMatrix()

    draw_canvas_border(canvas_margin)  #
    coda = str(int(random(10000)))  # hack to not overwrite when experimenting
    save("images/tile_rule_30_" + coda + ".png")

