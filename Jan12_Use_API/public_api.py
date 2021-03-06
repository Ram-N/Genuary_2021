"""
GENUARY 2021 - Public API
Use Surise and Sunset times for today to plot.

Ram Narasimhan
Jan12 2021

"""

from datetime import datetime
from grid import Grid

# from data import timings

w, h = 1080, 1080
margin = 20

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


def render_background():
    ystep = 20
    num = height / ystep
    noStroke()
    for ry in range(int(num)):
        fill(ry, 31, 49, 150 - ry)
        rect(0, ry * ystep, width, ystep)


bg_color = 120

g = Grid(6, 6, w, h, 0, 0)


def render_form_in_cell(c, mer, mer_values):

    blue_shade = (173 - abs(mer) / 3, 207 - abs(mer) / 3, 230)
    stroke(230)
    c.fill_cell(blue_shade)

    pushMatrix()
    translate(c.nwx, c.nwy)
    noFill()
    strokeWeight(7)
    stroke("#ffb144")
    ellipse(c.width / 2, c.height / 2, c.width / 1.3, c.width / 1.3)

    # we have 18 values for latitudes. 90 to -90
    # draw horizontal lines, one for each lat. length maps to duration.
    # yaxis maps to latitude

    strokeWeight(4)
    shift_flag = 0
    for lat_values in mer_values[:-1]:
        lat = (lat_values[0] + 90) // 10
        ssd = lat_values[1][0]
        sr, ss, dur = ssd
        if sr > 900:
            shift_flag = 1
            break

    for lat_values in mer_values[:-1]:
        lat = (lat_values[0] + 90) // 10
        ssd = lat_values[1][0]
        sr, ss, dur = ssd

        line_len = dur / 1200.0 * c.width
        sinc, binc = dur // 50, dur // 8
        stroke(74 - sinc, 208 - binc, 255 - sinc)
        # xstart = (c.width - line_len) / 2
        xstart = sr / 1440.0 * c.width
        # if shift_flag:
        #     xstart -= c.width / 2

        line(xstart, c.gh * lat, xstart + line_len, c.gh * lat)

        # handle wraparound
        if xstart + line_len > c.width:
            tail = xstart + line_len - c.width
            line(0, c.gh * lat, tail, c.gh * lat)

    fill(40)
    print(mer, "mer")
    text(str(mer), 10, 15)

    popMatrix()


def setup():
    size(w, h)
    stroke(240)
    g.render_cell_borders()
    #    background(bg_color)

    # render_background()  # background

    meridians = [
        -180,
        -170,
        -160,
        -150,
        -140,
        -130,
        -120,
        -110,
        -100,
        -90,
        -80,
        -70,
        -60,
        -50,
        -40,
        -30,
        -20,
        -10,
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90,
        100,
        110,
        120,
        130,
        140,
        150,
        160,
        170,
        180,
    ]

    for mi, c in enumerate(g.cells):
        # c.render_gridlines()
        mer = meridians[mi]
        render_form_in_cell(c, mer, timings[mer])

    stroke(240)
    strokeWeight(4)
    noFill()
    g.render_cell_borders()

    # draw_canvas_border(30, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "daylight_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)


timings = {
    -180: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(910, 548, 1078)]),
        (-50, [(972, 486, 954)]),
        (-40, [(1008, 450, 882)]),
        (-30, [(1033, 425, 832)]),
        (-20, [(1053, 406, 793)]),
        (-10, [(1070, 389, 759)]),
        (10, [(1101, 357, 696)]),
        (20, [(1118, 341, 663)]),
        (30, [(1137, 322, 625)]),
        (40, [(1160, 298, 578)]),
        (50, [(1193, 265, 512)]),
        (60, [(1248, 210, 402)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -170: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(870, 508, 1078)]),
        (-50, [(932, 446, 954)]),
        (-40, [(968, 410, 882)]),
        (-30, [(993, 385, 832)]),
        (-20, [(1013, 366, 793)]),
        (-10, [(1030, 349, 759)]),
        (10, [(1061, 317, 696)]),
        (20, [(1078, 301, 663)]),
        (30, [(1097, 282, 625)]),
        (40, [(1120, 258, 578)]),
        (50, [(1153, 225, 512)]),
        (60, [(1208, 170, 402)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -160: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(830, 468, 1078)]),
        (-50, [(892, 406, 954)]),
        (-40, [(928, 370, 882)]),
        (-30, [(953, 345, 832)]),
        (-20, [(973, 326, 793)]),
        (-10, [(990, 309, 759)]),
        (10, [(1021, 277, 696)]),
        (20, [(1038, 261, 663)]),
        (30, [(1057, 242, 625)]),
        (40, [(1080, 218, 578)]),
        (50, [(1113, 185, 512)]),
        (60, [(1168, 130, 402)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -150: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(790, 428, 1078)]),
        (-50, [(852, 366, 954)]),
        (-40, [(888, 330, 882)]),
        (-30, [(913, 305, 832)]),
        (-20, [(933, 286, 793)]),
        (-10, [(950, 269, 759)]),
        (10, [(981, 237, 696)]),
        (20, [(998, 221, 663)]),
        (30, [(1017, 202, 625)]),
        (40, [(1040, 178, 578)]),
        (50, [(1073, 145, 512)]),
        (60, [(1128, 90, 402)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -140: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(750, 388, 1078)]),
        (-50, [(812, 326, 954)]),
        (-40, [(848, 290, 882)]),
        (-30, [(873, 265, 832)]),
        (-20, [(893, 246, 793)]),
        (-10, [(910, 229, 759)]),
        (10, [(941, 197, 696)]),
        (20, [(958, 181, 663)]),
        (30, [(977, 162, 625)]),
        (40, [(1000, 138, 578)]),
        (50, [(1033, 105, 512)]),
        (60, [(1089, 50, 401)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -130: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(710, 348, 1078)]),
        (-50, [(772, 286, 954)]),
        (-40, [(808, 250, 882)]),
        (-30, [(833, 225, 832)]),
        (-20, [(853, 206, 793)]),
        (-10, [(870, 189, 759)]),
        (10, [(901, 157, 696)]),
        (20, [(918, 140, 662)]),
        (30, [(937, 122, 625)]),
        (40, [(960, 98, 578)]),
        (50, [(993, 65, 512)]),
        (60, [(1049, 10, 401)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -120: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(670, 308, 1078)]),
        (-50, [(732, 246, 954)]),
        (-40, [(768, 210, 882)]),
        (-30, [(793, 185, 832)]),
        (-20, [(813, 166, 793)]),
        (-10, [(830, 149, 759)]),
        (10, [(861, 117, 696)]),
        (20, [(878, 100, 662)]),
        (30, [(897, 82, 625)]),
        (40, [(920, 58, 578)]),
        (50, [(953, 25, 512)]),
        (60, [(1009, 1410, 401)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -110: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(630, 268, 1078)]),
        (-50, [(692, 206, 954)]),
        (-40, [(728, 170, 882)]),
        (-30, [(753, 145, 832)]),
        (-20, [(773, 126, 793)]),
        (-10, [(790, 109, 759)]),
        (10, [(821, 77, 696)]),
        (20, [(838, 60, 662)]),
        (30, [(857, 42, 625)]),
        (40, [(880, 18, 578)]),
        (50, [(913, 1425, 512)]),
        (60, [(969, 1369, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -100: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(590, 229, 1079)]),
        (-50, [(652, 166, 954)]),
        (-40, [(688, 130, 882)]),
        (-30, [(713, 105, 832)]),
        (-20, [(733, 86, 793)]),
        (-10, [(750, 69, 759)]),
        (10, [(781, 37, 696)]),
        (20, [(798, 20, 662)]),
        (30, [(817, 1, 624)]),
        (40, [(840, 1418, 578)]),
        (50, [(873, 1385, 512)]),
        (60, [(929, 1329, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -90: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(549, 189, 1080)]),
        (-50, [(612, 126, 954)]),
        (-40, [(648, 90, 882)]),
        (-30, [(673, 65, 832)]),
        (-20, [(693, 46, 793)]),
        (-10, [(710, 28, 758)]),
        (10, [(741, 1437, 696)]),
        (20, [(758, 1420, 662)]),
        (30, [(777, 1401, 624)]),
        (40, [(800, 1378, 578)]),
        (50, [(833, 1345, 512)]),
        (60, [(889, 1289, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -80: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(509, 149, 1080)]),
        (-50, [(572, 86, 954)]),
        (-40, [(608, 50, 882)]),
        (-30, [(633, 25, 832)]),
        (-20, [(653, 6, 793)]),
        (-10, [(670, 1428, 758)]),
        (10, [(701, 1397, 696)]),
        (20, [(718, 1380, 662)]),
        (30, [(737, 1361, 624)]),
        (40, [(760, 1338, 578)]),
        (50, [(793, 1305, 512)]),
        (60, [(849, 1249, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -70: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(469, 109, 1080)]),
        (-50, [(532, 46, 954)]),
        (-40, [(568, 10, 882)]),
        (-30, [(593, 1425, 832)]),
        (-20, [(612, 1406, 794)]),
        (-10, [(630, 1388, 758)]),
        (10, [(661, 1357, 696)]),
        (20, [(678, 1340, 662)]),
        (30, [(697, 1321, 624)]),
        (40, [(720, 1298, 578)]),
        (50, [(753, 1265, 512)]),
        (60, [(809, 1209, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -60: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(429, 69, 1080)]),
        (-50, [(492, 6, 954)]),
        (-40, [(528, 1410, 882)]),
        (-30, [(553, 1385, 832)]),
        (-20, [(572, 1366, 794)]),
        (-10, [(590, 1348, 758)]),
        (10, [(621, 1317, 696)]),
        (20, [(638, 1300, 662)]),
        (30, [(657, 1281, 624)]),
        (40, [(680, 1258, 578)]),
        (50, [(713, 1225, 512)]),
        (60, [(769, 1169, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -50: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(389, 29, 1080)]),
        (-50, [(452, 1406, 954)]),
        (-40, [(488, 1370, 882)]),
        (-30, [(513, 1345, 832)]),
        (-20, [(532, 1326, 794)]),
        (-10, [(550, 1308, 758)]),
        (10, [(581, 1277, 696)]),
        (20, [(598, 1260, 662)]),
        (30, [(617, 1241, 624)]),
        (40, [(640, 1218, 578)]),
        (50, [(673, 1185, 512)]),
        (60, [(729, 1129, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -40: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(349, 1429, 1080)]),
        (-50, [(412, 1366, 954)]),
        (-40, [(448, 1330, 882)]),
        (-30, [(473, 1305, 832)]),
        (-20, [(492, 1286, 794)]),
        (-10, [(509, 1268, 759)]),
        (10, [(541, 1237, 696)]),
        (20, [(558, 1220, 662)]),
        (30, [(577, 1201, 624)]),
        (40, [(600, 1178, 578)]),
        (50, [(633, 1145, 512)]),
        (60, [(689, 1089, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -30: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(309, 1389, 1080)]),
        (-50, [(372, 1326, 954)]),
        (-40, [(408, 1290, 882)]),
        (-30, [(433, 1265, 832)]),
        (-20, [(452, 1246, 794)]),
        (-10, [(469, 1228, 759)]),
        (10, [(501, 1197, 696)]),
        (20, [(518, 1180, 662)]),
        (30, [(537, 1161, 624)]),
        (40, [(560, 1138, 578)]),
        (50, [(593, 1105, 512)]),
        (60, [(649, 1049, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -20: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(269, 1349, 1080)]),
        (-50, [(332, 1286, 954)]),
        (-40, [(368, 1250, 882)]),
        (-30, [(393, 1225, 832)]),
        (-20, [(412, 1206, 794)]),
        (-10, [(429, 1188, 759)]),
        (10, [(461, 1157, 696)]),
        (20, [(478, 1140, 662)]),
        (30, [(497, 1121, 624)]),
        (40, [(520, 1098, 578)]),
        (50, [(553, 1065, 512)]),
        (60, [(609, 1009, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    -10: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(229, 1309, 1080)]),
        (-50, [(292, 1246, 954)]),
        (-40, [(328, 1210, 882)]),
        (-30, [(353, 1185, 832)]),
        (-20, [(372, 1166, 794)]),
        (-10, [(389, 1148, 759)]),
        (10, [(421, 1117, 696)]),
        (20, [(438, 1100, 662)]),
        (30, [(457, 1081, 624)]),
        (40, [(480, 1058, 578)]),
        (50, [(513, 1025, 512)]),
        (60, [(569, 969, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    0: [],
    10: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(149, 1229, 1080)]),
        (-50, [(212, 1166, 954)]),
        (-40, [(247, 1130, 883)]),
        (-30, [(273, 1105, 832)]),
        (-20, [(292, 1086, 794)]),
        (-10, [(309, 1068, 759)]),
        (10, [(341, 1037, 696)]),
        (20, [(358, 1020, 662)]),
        (30, [(377, 1001, 624)]),
        (40, [(400, 978, 578)]),
        (50, [(433, 945, 512)]),
        (60, [(489, 889, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    20: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(109, 1189, 1080)]),
        (-50, [(172, 1126, 954)]),
        (-40, [(207, 1090, 883)]),
        (-30, [(233, 1065, 832)]),
        (-20, [(252, 1046, 794)]),
        (-10, [(269, 1028, 759)]),
        (10, [(301, 997, 696)]),
        (20, [(318, 980, 662)]),
        (30, [(337, 961, 624)]),
        (40, [(360, 938, 578)]),
        (50, [(393, 905, 512)]),
        (60, [(449, 849, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    30: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(69, 1149, 1080)]),
        (-50, [(132, 1086, 954)]),
        (-40, [(167, 1050, 883)]),
        (-30, [(192, 1025, 833)]),
        (-20, [(212, 1006, 794)]),
        (-10, [(229, 988, 759)]),
        (10, [(261, 957, 696)]),
        (20, [(278, 940, 662)]),
        (30, [(297, 921, 624)]),
        (40, [(320, 898, 578)]),
        (50, [(353, 864, 511)]),
        (60, [(409, 809, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    40: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(29, 1109, 1080)]),
        (-50, [(92, 1046, 954)]),
        (-40, [(127, 1010, 883)]),
        (-30, [(152, 985, 833)]),
        (-20, [(172, 966, 794)]),
        (-10, [(189, 948, 759)]),
        (10, [(221, 917, 696)]),
        (20, [(238, 900, 662)]),
        (30, [(257, 881, 624)]),
        (40, [(280, 857, 577)]),
        (50, [(313, 824, 511)]),
        (60, [(369, 769, 400)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    50: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1429, 1069, 1080)]),
        (-50, [(52, 1006, 954)]),
        (-40, [(87, 970, 883)]),
        (-30, [(112, 945, 833)]),
        (-20, [(132, 926, 794)]),
        (-10, [(149, 908, 759)]),
        (10, [(181, 877, 696)]),
        (20, [(198, 860, 662)]),
        (30, [(217, 841, 624)]),
        (40, [(240, 817, 577)]),
        (50, [(273, 784, 511)]),
        (60, [(329, 728, 399)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    60: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1388, 1029, 1081)]),
        (-50, [(11, 966, 955)]),
        (-40, [(47, 930, 883)]),
        (-30, [(72, 905, 833)]),
        (-20, [(92, 886, 794)]),
        (-10, [(109, 868, 759)]),
        (10, [(141, 837, 696)]),
        (20, [(158, 820, 662)]),
        (30, [(177, 801, 624)]),
        (40, [(200, 777, 577)]),
        (50, [(233, 744, 511)]),
        (60, [(289, 688, 399)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    70: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1348, 989, 1081)]),
        (-50, [(1411, 926, 955)]),
        (-40, [(7, 890, 883)]),
        (-30, [(32, 865, 833)]),
        (-20, [(52, 846, 794)]),
        (-10, [(69, 828, 759)]),
        (10, [(101, 797, 696)]),
        (20, [(118, 780, 662)]),
        (30, [(137, 761, 624)]),
        (40, [(160, 737, 577)]),
        (50, [(193, 704, 511)]),
        (60, [(249, 648, 399)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    80: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1308, 949, 1081)]),
        (-50, [(1371, 886, 955)]),
        (-40, [(1407, 850, 883)]),
        (-30, [(1432, 825, 833)]),
        (-20, [(12, 806, 794)]),
        (-10, [(29, 788, 759)]),
        (10, [(61, 757, 696)]),
        (20, [(78, 740, 662)]),
        (30, [(97, 721, 624)]),
        (40, [(120, 697, 577)]),
        (50, [(153, 664, 511)]),
        (60, [(209, 608, 399)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    90: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1268, 909, 1081)]),
        (-50, [(1331, 846, 955)]),
        (-40, [(1367, 811, 884)]),
        (-30, [(1392, 785, 833)]),
        (-20, [(1412, 766, 794)]),
        (-10, [(1429, 748, 759)]),
        (10, [(21, 717, 696)]),
        (20, [(38, 700, 662)]),
        (30, [(57, 681, 624)]),
        (40, [(80, 657, 577)]),
        (50, [(113, 624, 511)]),
        (60, [(169, 568, 399)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    100: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1228, 869, 1081)]),
        (-50, [(1291, 806, 955)]),
        (-40, [(1327, 771, 884)]),
        (-30, [(1352, 745, 833)]),
        (-20, [(1372, 726, 794)]),
        (-10, [(1389, 708, 759)]),
        (10, [(1421, 677, 696)]),
        (20, [(1438, 660, 662)]),
        (30, [(17, 641, 624)]),
        (40, [(40, 617, 577)]),
        (50, [(73, 584, 511)]),
        (60, [(129, 528, 399)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    110: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1188, 829, 1081)]),
        (-50, [(1251, 766, 955)]),
        (-40, [(1287, 731, 884)]),
        (-30, [(1312, 705, 833)]),
        (-20, [(1332, 686, 794)]),
        (-10, [(1349, 668, 759)]),
        (10, [(1381, 637, 696)]),
        (20, [(1398, 620, 662)]),
        (30, [(1417, 601, 624)]),
        (40, [(0, 577, 577)]),
        (50, [(34, 544, 510)]),
        (60, [(90, 488, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    120: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1148, 790, 1082)]),
        (-50, [(1211, 726, 955)]),
        (-40, [(1247, 691, 884)]),
        (-30, [(1272, 665, 833)]),
        (-20, [(1292, 646, 794)]),
        (-10, [(1309, 628, 759)]),
        (10, [(1341, 597, 696)]),
        (20, [(1358, 580, 662)]),
        (30, [(1377, 561, 624)]),
        (40, [(1400, 537, 577)]),
        (50, [(1434, 504, 510)]),
        (60, [(50, 448, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    130: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1108, 750, 1082)]),
        (-50, [(1171, 686, 955)]),
        (-40, [(1207, 651, 884)]),
        (-30, [(1232, 625, 833)]),
        (-20, [(1252, 605, 793)]),
        (-10, [(1269, 588, 759)]),
        (10, [(1301, 557, 696)]),
        (20, [(1318, 540, 662)]),
        (30, [(1337, 521, 624)]),
        (40, [(1360, 497, 577)]),
        (50, [(1394, 464, 510)]),
        (60, [(10, 408, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    140: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1068, 710, 1082)]),
        (-50, [(1131, 646, 955)]),
        (-40, [(1167, 611, 884)]),
        (-30, [(1192, 585, 833)]),
        (-20, [(1212, 565, 793)]),
        (-10, [(1229, 548, 759)]),
        (10, [(1261, 517, 696)]),
        (20, [(1278, 500, 662)]),
        (30, [(1297, 481, 624)]),
        (40, [(1320, 457, 577)]),
        (50, [(1354, 424, 510)]),
        (60, [(1410, 368, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    150: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(1028, 670, 1082)]),
        (-50, [(1091, 606, 955)]),
        (-40, [(1127, 571, 884)]),
        (-30, [(1152, 545, 833)]),
        (-20, [(1172, 525, 793)]),
        (-10, [(1189, 508, 759)]),
        (10, [(1221, 477, 696)]),
        (20, [(1238, 460, 662)]),
        (30, [(1257, 441, 624)]),
        (40, [(1280, 417, 577)]),
        (50, [(1314, 384, 510)]),
        (60, [(1370, 328, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    160: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(988, 630, 1082)]),
        (-50, [(1051, 567, 956)]),
        (-40, [(1087, 531, 884)]),
        (-30, [(1112, 505, 833)]),
        (-20, [(1132, 485, 793)]),
        (-10, [(1149, 468, 759)]),
        (10, [(1181, 437, 696)]),
        (20, [(1198, 420, 662)]),
        (30, [(1217, 401, 624)]),
        (40, [(1240, 377, 577)]),
        (50, [(1274, 344, 510)]),
        (60, [(1330, 288, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    170: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(948, 590, 1082)]),
        (-50, [(1011, 527, 956)]),
        (-40, [(1047, 491, 884)]),
        (-30, [(1072, 465, 833)]),
        (-20, [(1092, 445, 793)]),
        (-10, [(1109, 428, 759)]),
        (10, [(1141, 397, 696)]),
        (20, [(1158, 380, 662)]),
        (30, [(1177, 361, 624)]),
        (40, [(1200, 337, 577)]),
        (50, [(1234, 304, 510)]),
        (60, [(1290, 248, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
    180: [
        (-90, [(0, 0, 0)]),
        (-80, [(0, 0, 0)]),
        (-70, [(0, 0, 0)]),
        (-60, [(908, 550, 1082)]),
        (-50, [(971, 487, 956)]),
        (-40, [(1007, 451, 884)]),
        (-30, [(1032, 425, 833)]),
        (-20, [(1052, 405, 793)]),
        (-10, [(1069, 388, 759)]),
        (10, [(1101, 357, 696)]),
        (20, [(1118, 340, 662)]),
        (30, [(1137, 321, 624)]),
        (40, [(1160, 297, 577)]),
        (50, [(1194, 264, 510)]),
        (60, [(1250, 208, 398)]),
        (70, [(0, 0, 0)]),
        (80, [(0, 0, 0)]),
        (90, [(0, 0, 0)]),
    ],
}

