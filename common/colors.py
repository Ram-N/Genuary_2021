# updated Jan 15 2021


palette = [
    "#FE4019",  # red-orange
    "#f69e55",  # orange
    "#0B85CF",  # light blue
    "#FF5FB9",  # pink
    "#2ec4b6",  # teal
    "#FFA900",  # yellow
    "#e71d36",  # red
    "#ffffff",  # white
    "#36225E",  # dark blue
]

# Colour Blocking 3 Color Palette
palette = [
    "#ff0a0e",  # (255,10,14) # red
    "#cc000e",  # (204,0,14) # red3
    "#fbc2b5",  # (251,194,181) # pastel
    "#a13e17",  # (161,62,23) # brown
    "#fbc2b5",  # (251,194,181) # pastel
    "#fec196",  # (254,193,150)
]


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
    "#036440",
    "#037d50",
    "#049660",
    "#37c12",
    "#049515",
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
_palette = [val for pair in zip(reds, greens) for val in pair] + ["#989898"]


# Piet Mondrian Color Palette
BLACK = (0, 0, 0)
MOND_WHITE = (223, 224, 236)
MOND_RED = (162, 45, 40)
MOND_BLUE = (38, 71, 124)
MOND_YELLOW = (240, 217, 92)

RED, GREEN = (255, 0, 0), (0, 255, 0)
BLUE, BLACK = (0, 0, 255), (0, 0, 0)
PURPLE, CYAN, YELLOW = (255, 0, 255), (0, 255, 255), (255, 255, 0)
ORANGE = (255, 150, 0)
ROSE, TEAL = (255, 102, 204), (0, 128, 128)
BROWN = (165, 42, 42)
_COLORS = [
    MOND_WHITE,
    CYAN,
    ORANGE,
    BLUE,
    TEAL,
    GREEN,
    BLACK,
    PURPLE,
    RED,
    YELLOW,
    ROSE,
    BLACK,
]
COLORS = [ORANGE, RED, ORANGE, RED, MOND_BLUE, BLUE]
RED_COLORS = [MOND_YELLOW, ORANGE, RED]
BLUE_COLORS = [TEAL, BLUE, MOND_BLUE, BLUE]
BLACK_COLORS = [BLACK, GREEN, BLACK]

EYE_COLORS = [BLACK, MOND_WHITE, TEAL, MOND_WHITE, BROWN]

BG_COLORS = [MOND_WHITE, (123, 124, 123)]
