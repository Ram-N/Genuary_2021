"""
Created for Genuary2021
Jan 06 - Triangle Subdivision
Author: Ram Narasimhan

Steps
1. First draw a static ICO
2. Rotate it
3. Subdivide Triangles
"""
from math import sqrt

palette = [
    # "#FE4019", #orange
    "#36225E",  # dark blue
    # "#0B85CF",  # light blue
    "#e71d36",  # red
    "#ffffff",  # white
    "#FFA900",  # yellow

radius = sqrt(sq(1) + sq(phi))

# From wikipedia: coordinates are (0,±1,±ϕ), (±ϕ,0,±1), (±1,±ϕ,0)
v = [
    (0, 1, phi),  # 0 mid down front
    (0, -1, phi),  # 1 mid up front
    (0, 1, -phi),  # 2 mid down back
    (0, -1, -phi),  # 3 mid up back
    (phi, 0, 1),  # 4 right center front
    (phi, 0, -1),  # 5 right center back
    (-phi, 0, 1),  # 6 left center front
    (-phi, 0, -1),  # 7 left center back
    (1, phi, 0),  # 8 right down flat
    (1, -phi, 0),  # 9 right up flat
    (-1, phi, 0),  # 10 left down flat
    (-1, -phi, 0),  # 11 left up flat
]

# triangle vertex indices
# 20 'base' triangle indices
base_indices = [
    (11, 9, 1),
    (11, 9, 3),
    (11, 9, 3),
    (9, 1, 4),
    (9, 3, 5),
    (11, 1, 6),
    (11, 3, 7),
    (11, 6, 7),
    (9, 4, 5),
    (1, 0, 6),
    (1, 0, 4),
    (10, 8, 0),
    (10, 8, 2),
    (8, 0, 4),
    (8, 2, 5),
    (10, 0, 6),
    (10, 2, 7),
    (10, 6, 7),
    (8, 4, 5),
    (3, 2, 7),
    (3, 2, 5),
]


w, h = 1000, 1000
margin = 20
_scale = 200

TWO_PHI = 2 * phi * _scale
PHI = phi * _scale

# random colors, but fixed
col_ints = [int(random(len(palette))) for _ in range(20)]


def create_face_coordinates(base_indices):
    num_colors = len(palette)
    face_triangles = []
    fnum = 0
    for triplet_index in base_indices:
        a, b, c = triplet_index
        x0, y0, z0 = v[a][0] * _scale, v[a][1] * _scale, v[a][2] * _scale
        x1, y1, z1 = v[b][0] * _scale, v[b][1] * _scale, v[b][2] * _scale
        x2, y2, z2 = v[c][0] * _scale, v[c][1] * _scale, v[c][2] * _scale
        # _color = palette[fnum % num_colors]
        _color = palette[fnum % 4]

        face_triangles.append([(x0, y0, z0), (x1, y1, z1), (x2, y2, z2), _color])
        fnum += 1

    return face_triangles


# Given a set of 3-xyz, each one made up of triangles, plus a color
# Render them one by one
def render_ico(face_triangles):

    i = 0
    for triplet_coords in face_triangles:
        ta, tb, tc, _clr = triplet_coords
        x0, y0, z0 = ta
        x1, y1, z1 = tb
        x2, y2, z2 = tc
        fill(_clr)
        beginShape()
        vertex(x0, y0, z0)
        vertex(x1, y1, z1)
        vertex(x2, y2, z2)
        endShape()
        i += 1


# Let px be a point to be projected on the sphere
# c the sphere's centre and r the radius
# Unit vector is the correct direction is  (px-c)/(norm(px-c)
# then new point = c + r* unit_vector_of_p)
def divide_triangle_into_4(triplet_coords):

    t0, t1, t2, _clr = triplet_coords
    x0, y0, z0 = t0  # v0
    x1, y1, z1 = t1  # v1
    x2, y2, z2 = t2  # v2

    mx0 = (x0 + x1) * 0.5
    my0 = (y0 + y1) * 0.5
    mz0 = (z0 + z1) * 0.5
    mult = radius / sqrt(mx0 ** 2 + my0 ** 2 + mz0 ** 2) * _scale

    mx1 = (x2 + x1) * 0.5
    my1 = (y2 + y1) * 0.5
    mz1 = (z2 + z1) * 0.5
    mult = radius / sqrt(mx1 ** 2 + my1 ** 2 + mz1 ** 2) * _scale

    mx2 = (x0 + x2) * 0.5
    my2 = (y0 + y2) * 0.5
    mz2 = (z0 + z2) * 0.5
    mult = radius / sqrt(mx2 ** 2 + my2 ** 2 + mz2 ** 2) * _scale

    m0 = (mx0 * mult, my0 * mult, mz0 * mult)
    m1 = (mx1 * mult, my1 * mult, mz1 * mult)
    m2 = (mx2 * mult, my2 * mult, mz2 * mult)

    nts = []
    nts.append([t0, m0, m2])
    nts.append([t1, m1, m0])
    nts.append([t2, m2, m1])
    nts.append([m0, m1, m2])

    return nts


def subdivide_triangles(face_triangles):

    fnum = 0
    smaller_triangles = []
    for triplet_coords in face_triangles:
        new_triangles = divide_triangle_into_4(triplet_coords)

        for nt in new_triangles:
            smaller_triangles.append(nt)

    # Update the face_triangles
    # Add all the smaller triangles to face_triangles
    tnum = 0
    face_triangles = []
    for small_t in smaller_triangles:
        # new_color = palette[int(random(len(palette)))]
        new_color = palette[tnum % 4]
        v0, v1, v2 = small_t
        face_triangles.append((v0, v1, v2, new_color))
        tnum += 1

    return face_triangles


# get base coords xyz and color
face_ts = create_face_coordinates(base_indices)


def setup():
    size(w, h, P3D)
    frameRate(5)


def draw():

    global face_ts
    background(255)
    fill(127)
    rect(margin, margin, w - 2 * margin, h - 2 * margin)

    if frameCount == 50 or frameCount == 100 or frameCount == 150 or frameCount == 200:
        face_ts = subdivide_triangles(face_ts)

    translate(width / 2, height / 2, 0)
    rotateX(0.01 * frameCount)
    rotateY(0.01 * frameCount)

    stroke(10)
    strokeWeight(3)
    render_ico(face_ts)

    # if frameCount > 800 and not frameCount % 50:
    saveFrame("images/" + titlestr + "_####.png")

