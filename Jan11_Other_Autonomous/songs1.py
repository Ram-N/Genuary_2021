"""

GENUARY 2021 - Tree
Draw Song Spirals, one for each year. Upto 10 songs per Year.

Ram Narasimhan
Jan11 2021

"""
from datetime import datetime

w, h = 1040, 1040
margin = 20

# SPIRAL RELATED
NUM_POINTS = 140  # also, points in the spiral
MIN_RADIUS = 100

palette = [
    "#FE4019",  # orange
    "#36225E",  # dark blue
    "#e71d36",  # red
    "#0B85CF",  # light blue
    #    "#FF5FB9",  # pink
    "#2ec4b6",  # teal
    "#f69e55",  # orange
    "#FFA900",  # yellow
    "#ffffff",  # white
]


songs = [
    {"year": 2010, "rank": 1, "duration": "228293", "genre": "pop"},
    {"year": 2010, "rank": 3, "duration": "239600", "genre": "rock"},
    {"year": 2010, "rank": 4, "duration": "220733", "genre": "pop"},
    {"year": 2010, "rank": 5, "duration": "235493", "genre": "r&b"},
    {"year": 2010, "rank": 6, "duration": "547733", "genre": "rap"},
    {"year": 2010, "rank": 7, "duration": "227880", "genre": "pop"},
    {"year": 2010, "rank": 8, "duration": "211080", "genre": "rock"},
    {"year": 2010, "rank": 9, "duration": "236253", "genre": "pop"},
    {"year": 2010, "rank": 10, "duration": "243533", "genre": "r&b"},
    {"year": 2011, "rank": 1, "duration": "244885", "genre": "pop"},
    {"year": 2011, "rank": 2, "duration": "260467", "genre": "pop"},
    {"year": 2011, "rank": 3, "duration": "263360", "genre": "edm"},
    {"year": 2011, "rank": 4, "duration": "250627", "genre": "rock"},
    {"year": 2011, "rank": 5, "duration": "201160", "genre": "pop"},
    {"year": 2011, "rank": 6, "duration": "215760", "genre": "r&b"},
    {"year": 2011, "rank": 7, "duration": "285040", "genre": "pop"},
    {"year": 2011, "rank": 8, "duration": "252307", "genre": "rap"},
    {"year": 2011, "rank": 9, "duration": "199480", "genre": "edm"},
    {"year": 2011, "rank": 10, "duration": "193400", "genre": "pop"},
    {"year": 2012, "rank": 1, "duration": "219493", "genre": "pop"},
    {"year": 2012, "rank": 2, "duration": "231467", "genre": "pop"},
    {"year": 2012, "rank": 3, "duration": "225200", "genre": "r&b"},
    {"year": 2012, "rank": 4, "duration": "200187", "genre": "pop"},
    {"year": 2012, "rank": 5, "duration": "233478", "genre": "pop"},
    {"year": 2012, "rank": 6, "duration": "210813", "genre": "rap"},
    {"year": 2012, "rank": 7, "duration": "255587", "genre": "pop"},
    {"year": 2012, "rank": 8, "duration": "232907", "genre": "r&b"},
    {"year": 2012, "rank": 9, "duration": "200747", "genre": "r&b"},
    {"year": 2012, "rank": 10, "duration": "163133", "genre": "rock"},
    {"year": 2013, "rank": 1, "duration": "369627", "genre": "edm"},
    {"year": 2013, "rank": 2, "duration": "263053", "genre": "r&b"},
    {"year": 2013, "rank": 3, "duration": "232578", "genre": "pop"},
    {"year": 2013, "rank": 4, "duration": "190185", "genre": "unknown"},
    {"year": 2013, "rank": 5, "duration": "250907", "genre": "rap"},
    {"year": 2013, "rank": 6, "duration": "484147", "genre": "r&b"},
    {"year": 2013, "rank": 7, "duration": "204053", "genre": "rap"},
    {"year": 2013, "rank": 8, "duration": "223546", "genre": "pop"},
    {"year": 2013, "rank": 9, "duration": "257267", "genre": "rap"},
    {"year": 2013, "rank": 10, "duration": "227880", "genre": "pop"},
    {"year": 2014, "rank": 2, "duration": "281560", "genre": "pop"},
    {"year": 2014, "rank": 4, "duration": "172724", "genre": "pop"},
    {"year": 2014, "rank": 5, "duration": "219209", "genre": "pop"},
    {"year": 2014, "rank": 6, "duration": "219043", "genre": "edm"},
    {"year": 2014, "rank": 7, "duration": "199080", "genre": "rock"},
    {"year": 2014, "rank": 8, "duration": "187920", "genre": "pop"},
    {"year": 2014, "rank": 10, "duration": "193893", "genre": "pop"},
    {"year": 2015, "rank": 1, "duration": "295502", "genre": "pop"},
    {"year": 2015, "rank": 2, "duration": "267024", "genre": "rap"},
    {"year": 2015, "rank": 3, "duration": "215613", "genre": "r&b"},
    {"year": 2015, "rank": 4, "duration": "219333", "genre": "rap"},
    {"year": 2015, "rank": 5, "duration": "234693", "genre": "rap"},
    {"year": 2015, "rank": 6, "duration": "159359", "genre": "pop"},
    {"year": 2015, "rank": 7, "duration": "252539", "genre": "pop"},
    {"year": 2015, "rank": 8, "duration": "206880", "genre": "pop"},
    {"year": 2015, "rank": 9, "duration": "188238", "genre": "r&b"},
    {"year": 2015, "rank": 10, "duration": "207547", "genre": "pop"},
    {"year": 2016, "rank": 1, "duration": "230453", "genre": "r&b"},
    {"year": 2016, "rank": 2, "duration": "173975", "genre": "rap"},
    {"year": 2016, "rank": 3, "duration": "244960", "genre": "edm"},
    {"year": 2016, "rank": 4, "duration": "206693", "genre": "pop"},
    {"year": 2016, "rank": 5, "duration": "195920", "genre": "pop"},
    {"year": 2016, "rank": 6, "duration": "219320", "genre": "r&b"},
    {"year": 2016, "rank": 7, "duration": "211667", "genre": "pop"},
    {"year": 2016, "rank": 8, "duration": "203686", "genre": "pop"},
    {"year": 2016, "rank": 9, "duration": "225983", "genre": "pop"},
    {"year": 2016, "rank": 10, "duration": "200187", "genre": "unknown"},
    {"year": 2017, "rank": 1, "duration": "233713", "genre": "pop"},
    {"year": 2017, "rank": 3, "duration": "247627", "genre": "edm"},
    {"year": 2017, "rank": 5, "duration": "218320", "genre": "rap"},
    {"year": 2017, "rank": 6, "duration": "259550", "genre": "pop"},
    {"year": 2017, "rank": 7, "duration": "288877", "genre": "rap"},
    {"year": 2017, "rank": 8, "duration": "163253", "genre": "rock"},
    {"year": 2017, "rank": 9, "duration": "187147", "genre": "rock"},
    {"year": 2017, "rank": 10, "duration": "199849", "genre": "pop"},
    {"year": 2018, "rank": 3, "duration": "165853", "genre": "rock"},
    {"year": 2018, "rank": 7, "duration": "231787", "genre": "pop"},
    {"year": 2018, "rank": 8, "duration": "210653", "genre": "rap"},
    {"year": 2018, "rank": 9, "duration": "232293", "genre": "rock"},
    {"year": 2019, "rank": 4, "duration": "221480", "genre": "pop"},
    {"year": 2019, "rank": 10, "duration": "149242", "genre": "rap"},
]


def render_spiral(spiral_center, spiral_radius, num_points=NUM_POINTS):
    """ Draw the Spiral in reverse, from out to in """

    fill(0)
    scx, scy = spiral_center
    pushMatrix()
    translate(scx, scy)
    radius_inc = (spiral_radius - MIN_RADIUS) / (num_points + 2)
    theta_inc = 1.8 * TWO_PI / (num_points + 1)

    ellipse(0, 0, 10, 10)

    r = spiral_radius
    theta = PI / 2 * 1.2
    centers = []
    for _ in range(num_points):
        fill(0)

        x = r * cos(theta)
        y = r * sin(theta)
        centers.append((scx + x, scy + y))
        ellipse(x, y, 10, 10)

        theta -= theta_inc  # Decrement the angle
        r -= radius_inc  # Decrement the radius
    popMatrix()

    print(len(centers), "length")

    return centers


def render_background():
    ystep = 20
    num = height / ystep
    noStroke()
    for ry in range(int(num)):
        fill(ry, 31, 49, 150 - ry)
        rect(0, ry * ystep, width, ystep)

    # textSize(14)
    # text("#Genuary2021, Jan-10th", width - 200, height - 25)


color_d = {"rap": 0, "r&b": 1, "edm": 2, "unknown": 3, "pop": 4, "rock": 5}

r_step = 8


def render_year_bubble(sc, year):
    """

    Radius of strip depends on ranking...
    """

    noFill()
    scx, scy = sc
    pushMatrix()
    translate(scx, scy)

    angles = []
    ranks, genres = [], []
    ranksum = {}  # dict of sum of ranks, by year
    for sd in songs:
        if sd["year"] == year:
            # print(sd)
            secs = int(sd["duration"]) / 1000
            angles.append(secs / 360.0 * TWO_PI)
            r_int = int(sd["rank"])
            ranks.append(r_int)
            if year in ranksum:
                ranksum[year] += r_int
            else:
                ranksum[year] = r_int
            genres.append(sd["genre"])

    start = 0
    radius = 100
    for q in range(len(angles)):
        r = 15 - q
        start = start
        stop = start + angles[-1 - q]
        fill(bg_color)
        radius = (r_step * r) + (ranks[-1 - q] - 1) * 10
        # print(r, radius, ranks[-1 - q])
        ellipse(0, 0, radius, radius)
        fill(palette[color_d[genres[-1 - q]]])
        arc(0, 0, radius, radius, start, stop)
        start = stop

    fill(bg_color)
    ellipse(0, 0, radius - r_step, radius - r_step)

    popMatrix()


bg_color = 201


def setup():
    size(w, h)
    background(bg_color)

    render_background()  # background
    num_points = 9
    sp_rad = 450
    centers = render_spiral((width / 2, (height / 2) - 20), sp_rad, num_points)
    print(centers)

    stroke(10)
    for ynum in range(8, -1, -1):
        sc = (centers[ynum][0], centers[ynum][1])
        render_year_bubble(sc, 2019 - ynum)
        print(sc, 2019 - ynum)

    stroke(10, 20, 30, 100)
    strokeWeight(6)
    for idx, c in enumerate(centers[:-1]):
        nx, ny = centers[idx + 1][0], centers[idx + 1][1]
        line(c[0], c[1], nx, ny)

    line(nx, ny, width / 2, (height / 2) - 20)

    draw_canvas_border(20, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "spiral_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

