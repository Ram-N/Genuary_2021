"""
GENUARY 2021 - "Subdivision"
Use Sphinx Tiles to Subdivide

Ram Narasimhan
Jan14 2021

"""

from datetime import datetime

margin = 0
w, h, = 1056, 1056
wm, hm = w + 2 * margin, h + 2 * margin

palette = [
    "#FE4019",  # orange
    "#36225E",  # dark blue
    "#e71d36",  # red
    "#0B85CF",  # light blue
    "#FF5FB9",  # pink
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


cell_mesh_sq = 8
JN_POINT = [2, cell_mesh_sq - 2]


def draw_sphinx((x0,y0), chirality='R', size=1, _rotation=0,  flip=False, fc=None):
    """

        _rotation in integer sets of 60 degrees. 0 to 5
    """

    print('attempting to draw', size, chirality, (x0, y0), _rotation)
    sw, sh = tw * size, th * size
    _rotation += 3

    pushStyle()
    if fc:
        r,g,b = fc
        fill(r,g,b, 100)

    flip = -1 if chirality=='L' else 1

    pushMatrix()
    translate(x0, y0)
    rotate(_rotation * PI / 3)
    x1, y1 = sw * flip, 2 * sh
    x2, y2 = 1.5 * sw * flip, sh
    x3, y3 = 2.5 * sw * flip, sh
    x4, y4 = 3 * sw * flip, 0


    beginShape()
    vertex(0, 0)
    vertex(x1, y1)
    vertex(x2, y2)
    vertex(x3, y3)
    vertex(x4, y4)
    endShape(CLOSE)

    popMatrix()
    popStyle()



color_d = {('L', 2):(210,120,0), ('R', 2):(30,10,0),
('L', 4):(220,110,0), ('R', 4):(25,10,0),
('L', 6):(230,100,0), ('R', 6):(20,10,0),
('L', 8):(240,90,0), ('R', 8):(15,10,0),
('L', 10):(250,80,0), ('R', 10):(10,10,0),
('L', 0):(200,130,0), ('R', 0):(0,10,0)}


def dissect((x0,y0), chirality='L', size=1, _rotation=0):
    """
    Dissect a Sphinx of given chirality, orientation based at x0, y0 of size into 4 smaller sphinxes.
    Return their properties (Chiral, orient, base, size)

    chirality = L or R, of the parent.
    size is the bigger sphinx incoming, in triangle-lengths
    Rotation is the orientation (0 to 6) of the original Larger Sphinx
    """

    if size == 1:
        return [] #no need to dissect further
    size/=2 #step down 1 in size


    bigsize = size*2
    flip = 1
    ch0, ch1, ch2, ch3 = 'R','R','R','L'
    rot3 = 2
    if chirality == 'R':
        ch0, ch1, ch2, ch3 = 'L','L','L','R'
        rot3 = 4 #4th tile
        flip = -1

    pushMatrix()
    translate(x0, y0)
    ellipse(0,0,10,10)

    #draw outline of larger sphinx
    pushStyle()
    noFill()
    strokeWeight(bigsize)
    col_ = color_d[(chirality, _rotation)]
    draw_sphinx((0,0), chirality, size=bigsize, _rotation=0, fc=col_)  # outline
    popStyle()

    x1, y1 = 3 * size*tw * flip, 0
    x2, y2 = -size*tw * flip, -2*size*th
    x3, y3 = -size*tw * flip, -4*size*th

    # draw_sphinx((0,0), ch0, size=size, _rotation=0, fc=(230,130,0))  # start
    # draw_sphinx((x1,y1), ch1, size=size, _rotation=0, fc=(130,230,0))  # east of start
    # draw_sphinx((x2,y2), ch2, size=size, _rotation=3)  # upside down
    # draw_sphinx((x3,y3), ch3,  size=size, _rotation=rot3,fc=(0,0,200)) 
    popMatrix()

    sw, sh = size*tw, size*th
    yshift = 8*sh


    #0 and 'R'
    if (_rotation%12)==0 and chirality == 'L':        
        xshift = 3*sw
        s0 = ((x0+xshift,y0), ch0, size, _rotation)
        s1 = ((x1+xshift,y1), ch1, size, _rotation)
        s2 = ((x2+xshift,y2), ch2, size, 6+ _rotation)
        s3 = ((x3+xshift,y3), ch3, size, rot3+2 + _rotation)
        return (s0,s1, s2, s3)

    if (_rotation%12)==0 and chirality == 'L':        
        s0 = ((x0-6*sw,y0), ch0, size, _rotation)
        s1 = ((x1-6*sw,y1), ch1, size, _rotation)
        s2 = ((x2-sw,y2+4*sh), ch2, size, 6+ _rotation)
        s3 = ((x3-sw,y3+8*sh), ch3, size, rot3+2 + _rotation)
        return (s0,s1, s2, s3)


    if (_rotation%12)==4 and chirality == 'L':        
        xshift = 3*sw
        s0 = ((x0-3*sw,y0+6*sh), ch0, size, _rotation)
        s1 = ((x1-4.5*sw,y1+3*sh), ch1, size, _rotation)
        s2 = ((x2+1.5*sw,y2+5*sh), ch2, size, 6+ _rotation)
        s3 = ((x3+3*sw,y3+8*sh), ch3, size, rot3+2 + _rotation)
        return (s0,s1, s2, s3)

    if (_rotation%12)==6 and chirality == 'L':        
        s0 = ((x0-6*sw,y0), ch0, size, _rotation)
        s1 = ((x1-6*sw,y1), ch1, size, _rotation)
        s2 = ((x2-sw,y2+4*sh), ch2, size, 6+ _rotation)
        s3 = ((x3-sw,y3+8*sh), ch3, size, rot3+2 + _rotation)
        return (s0,s1, s2, s3)

    if (_rotation%12)==2 and chirality == 'R':        
        s0 = ((x0-3*sw,y0-6*sh), ch0, size, _rotation)
        s1 = ((x1+1.5*sw,y1-3*sh), ch1, size, _rotation)
        s2 = ((x2-0.5*sw,y2-sh), ch2, size, 6+ _rotation)
        s3 = ((x3+sw,y3), ch3, size, rot3+4 + _rotation)
        return (s0,s1, s2, s3)

    if (_rotation%12)==6 and chirality == 'R':        #upside down R
        s0 = ((x0+6*sw,y0), ch0, size, _rotation)
        s1 = ((x1+6*sw,y1), ch1, size, _rotation)
        s2 = ((x2+sw,y2+4*sh), ch2, size, 6+ _rotation)
        s3 = ((x3+sw,y3+8*sh), ch3, size, rot3+4 + _rotation)
        return (s0,s1, s2, s3)


    if (_rotation%12)==8 and chirality == 'R':        
        s0 = ((x0+3*sw,y0+6*sh), ch0, size, _rotation)
        s1 = ((x1+4.5*sw,y1+3*sh), ch1, size, _rotation)
        s2 = ((x2-1.5*sw,y2+5*sh), ch2, size, 6+ _rotation)
        s3 = ((x3-3*sw,y3+8*sh), ch3, size, rot3+4 + _rotation)
        return (s0,s1, s2, s3)




    print('didnt find ', _rotation, chirality)

    #R and 0
    s0 = ((x0-3*sw,y0), ch0, size, _rotation)
    s1 = ((x1-3*sw,y1), ch1, size, _rotation)
    s2 = ((x2-3*sw,y2), ch2, size, 6+ _rotation)
    s3 = ((x3-3*sw,y3), ch3, size, rot3+4 + _rotation)
    return (s0,s1, s2, s3)



def subdivide((x0,y0), chirality='L', size=1, _rotation=0):

    pushMatrix()
    translate(x0, y0)
    rotate(PI/6 * _rotation) #orient big Sphinx to align, and _then_ subdivide
    subs = dissect((0,0), chirality, size, _rotation)
    popMatrix()

#    print('x0y0', x0, y0)
#    print('Larger size and chi', size, chirality)
    for s in subs:
#        print('Larger size and chi', size, chirality, 'smaller', s)
        subxy, chi, ssize, srot = s
        sx, sy = subxy
        srot = srot%12
        subs = subdivide((sx+x0, sy+y0), chi, ssize, _rotation=srot)


    return subs


bg_color = 250

tw = 32
th = tw * cos(PI / 6)

num_cols = int(w / tw)
num_rows = int(h / th)

####################################

def setup():
    size(wm, hm)  # including margin
    background(bg_color)
    stroke(40)

    dots = []
    for col in range(num_cols):
        row_dots = []
        for row in range(num_rows):
            p = PVector()
            xoffset = 0 if row % 2 else tw / 2
            x = col * tw + xoffset
            y = row * th
            #ellipse(x, y, 5, 5)
            p.x, p.y = x, y
            p.row, p.col = row, col
            row_dots.append(p)
        dots.append(row_dots)

    print(num_rows, num_cols, len(dots))

    size = 8
    xadj, yadj = 0, 10

    sx, sy = 0, 10
    x0, y0 = dots[sx][sy].x, dots[sx][sy].y
    subs = subdivide((x0,y0), 'R', size, _rotation=6)

    sx, sy = 32, 26
    x0, y0 = dots[sx][sy].x, dots[sx][sy].y
    subs = subdivide((x0,y0), 'R', size, _rotation=0)

    # sx, sy = xadj-28,yadj
    # x0, y0 = dots[sx][sy].x, dots[sx][sy].y
    # subs = subdivide((x0,y0), 'R', size, _rotation=2)


    # draw_canvas_border(30, border_color=220)  #
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    titlestr = "sphinx1_"
    save("images/" + titlestr + timestamp + ".png")


def draw_canvas_border(grid_margin, border_color=255):
    strokeWeight(grid_margin)
    noFill()
    stroke(border_color)
    rect(0, 0, w, h)

