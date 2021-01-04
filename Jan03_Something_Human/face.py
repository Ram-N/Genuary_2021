"""

Created for Genuary2021.
Something human.

Author: Ram Narasimhan

"""
from colors import EYE_COLORS


def two_epsilon(gw):
    return random(1) * gw * 0.5


def xadj(gw):
    pullback = gw * 0.25
    return two_epsilon(gw) - pullback


def yadj(gh):
    pullback = gh * 0.25
    return two_epsilon(gh) - pullback


class Face(object):
    def __init__(self, _cx, _cy, cell):
        self.cx, self.cy = _cx, _cy  # face center, 0,0

        epsilon = random(1) * cell.gw * 0.25
        gw = cell.gw
        gh = cell.gh
        pullback = gw * 0.25

        self.x_left_sq = cell.gw * -4 - pullback + two_epsilon(gw)
        self.x_right_sq = cell.gw * 4 - pullback + two_epsilon(gw)

        # EYES
        self.eye_len = 2 * cell.gw
        self.x_left_eye_end, self.x_left_eye_start = cell.gw * -3, -cell.gw
        self.x_right_eye_end, self.x_right_eye_start = cell.gw * 3, cell.gw

        # BROW
        brow = gw * 3 - pullback + two_epsilon(gw)

        self.x_left_brow_end, self.x_left_brow_start = -brow, -gw
        self.x_right_brow_end, self.x_right_brow_start = brow, gw

        self.y_hairtop = -6 * cell.gh + yadj(gh)
        self.y_hairmid = -4 * cell.gh + yadj(gh)
        self.y_hair = -3 * cell.gh + yadj(gh)
        self.y_temple = -2 * gh + yadj(gh)
        self.y_brow = -cell.gh + yadj(gh)
        self.y_ear_top = -cell.gh + yadj(gh)
        self.y_ear_start = 0 + yadj(gh)
        self.eye_upper = -0.5 * cell.gh + yadj(gh)
        self.y_eyeline = 0 + yadj(gh)
        self.eye_lower = 0.5 * cell.gh + yadj(gh)
        self.y_nose = 1.5 * cell.gh + yadj(gh)

        self.y_ear_bottom = 2 * cell.gh + yadj(gh)
        self.y_upper_lip = 2 * cell.gh + yadj(gh)
        self.y_mouth = 2.5 * cell.gh + yadj(gh)
        self.y_mouth_smile = 2.75 * cell.gh
        self.y_lower_lip = 3 * cell.gh

        # CHIN
        self.y_chintip = 5 * gh - pullback + two_epsilon(gh)
        self.y_low = 6 * gh - pullback + two_epsilon(gh)

        self.xchin_L, self.xchin_R = -gw * 2 + xadj(gw), gw * 2 + xadj(gw)

        self.x_mouth_L, self.x_mouth_R = -self.eye_len, self.eye_len

        self.x_ear_LS, self.x_ear_RS = cell.gw * -4, cell.gw * 4
        self.x_ear_LE = cell.gw * -5.5 + xadj(gw)
        self.x_ear_RE = cell.gw * 5.5 + xadj(gw)

        if random(1) < 0.33:
            ellipse(0, 0, 5, 5)

    def draw_face(self, cell):

        outline(self)
        eyes(self, cell)
        pushStyle()
        strokeWeight(4)
        hair(self)
        popStyle()
        ears(self, cell)
        mouth(self, cell)

    def eye_brows(self, cell):
        pushStyle()
        strokeWeight(2 + int(random(7)))
        noFill()
        gh = cell.gh
        BR1 = 0.7 + random(1) * 0.2
        bezier(
            self.x_right_brow_end,
            self.y_brow,
            self.x_right_brow_end * BR1,
            self.y_brow - gh * 0.5,
            self.x_right_brow_end * 0.7,
            self.y_brow - gh * 0.5,
            self.x_right_brow_start,
            self.y_brow,
        )

        bezier(
            self.x_left_brow_end,
            self.y_brow,
            self.x_left_brow_end * BR1,
            self.y_brow - cell.gh * 0.5,
            self.x_left_brow_end * 0.7,
            self.y_brow - cell.gh * 0.5,
            self.x_left_brow_start,
            self.y_brow,
        )

        # ellipse(self.x_right_eye_start + self.eye_len, self.y_brow, 5, 5)
        popStyle()


def nose_line(face):

    if random(1) < 0.5:
        pushStyle()
        strokeWeight(3)
        line(face.x_left_eye_start, face.y_nose, face.x_right_eye_start, face.y_nose)
        popStyle()


def draw_sides(face):
    pushStyle()
    strokeWeight(4)
    color(200)
    line(face.x_left_sq, face.y_hair, face.x_left_sq, face.y_nose)
    line(face.x_right_sq, face.y_hair, face.x_right_sq, face.y_nose)
    popStyle()
    noFill()


def outline(face):
    draw_sides(face)
    nose_line(face)
    pushStyle()
    strokeWeight(4)
    chin(face)
    popStyle()


def chin(face):
    # bezier from rt_nose to chintip
    # bezier from left_nose to chintip
    chin_dist = face.y_chintip - face.y_nose
    bezier(
        face.x_left_sq,
        face.y_nose,
        face.x_left_sq * 1.1,
        face.y_nose + chin_dist * 0.7,
        face.xchin_L * 1.8,
        face.y_nose + chin_dist * 0.5,
        face.xchin_L,
        face.y_chintip,
    )

    # right chin line
    bezier(
        face.x_right_sq,
        face.y_nose,
        face.x_right_sq * 1.1,
        face.y_nose + chin_dist * 0.7,
        face.xchin_R * 1.8,
        face.y_nose + chin_dist * 0.5,
        face.xchin_R,
        face.y_chintip,
    )

    # chin cup
    bezier(
        face.xchin_L,
        face.y_chintip,
        0,
        face.y_low,
        0,
        face.y_low,
        face.xchin_R,
        face.y_chintip,
    )


def eyes(face, cell):
    face.eye_brows(cell)

    gw = cell.gw
    pushStyle()
    strokeWeight(3)

    eyecolor = EYE_COLORS[int(random(5))]

    for e in range(2):
        x_EE = face.x_left_eye_end if e else face.x_right_eye_end
        x_ES = face.x_left_eye_start if e else face.x_right_eye_start

        x_eye_center = x_ES + (x_EE - x_ES) / 3 + xadj(gw)
        fill(*eyecolor)
        ellipse(x_eye_center, face.y_eyeline, cell.gh / 2, gw / 2)
        noFill()

        for yside in range(2):
            y_Eht = face.eye_lower if yside else face.eye_upper

            bezier(
                x_EE,
                face.y_eyeline,
                x_EE * 0.5,
                y_Eht,
                x_EE * 0.5,
                y_Eht,
                x_ES,
                face.y_eyeline,
            )

    popStyle()


def mouth(face, cell):

    pushStyle()
    strokeWeight(3)
    stroke(200, 0, 100)

    # mouth line...
    bezier(
        face.x_mouth_L,
        face.y_mouth,
        0,
        face.y_mouth_smile,
        0,
        face.y_mouth_smile,
        face.x_mouth_R,
        face.y_mouth,
    )

    lower_lip, upper_lip = False, False
    if random(1) > 0.5:
        upper_lip = True
    if random(1) > 0.5:
        lower_lip = True

    for e in range(2):
        x_mouth = face.x_mouth_L if e else face.x_mouth_R
        if upper_lip:
            bezier(
                x_mouth,
                face.y_mouth,
                x_mouth * 0.5,
                face.y_upper_lip,
                x_mouth * 0.3,
                face.y_upper_lip,
                0,
                (face.y_upper_lip + face.y_mouth) / 2,
            )

        if lower_lip:
            bezier(
                x_mouth,
                face.y_mouth,
                x_mouth * 0.5,
                face.y_lower_lip,
                x_mouth * 0.3,
                face.y_lower_lip,
                0,
                face.y_lower_lip,
            )

    popStyle()


def hair_line(face):

    self = face
    bezier(
        self.x_left_sq,
        self.y_temple,
        0,
        self.y_hairtop,
        self.x_right_sq,
        self.y_hairtop,
        self.x_right_sq,
        self.y_temple,
    )  # hair box top


def hair(face):
    hair_line(face)

    # two beziers... one long one short..
    bezier(
        face.x_left_sq,
        face.y_hair,
        0,
        face.y_hairtop,
        0,
        face.y_hairtop,
        face.x_right_sq,
        face.y_hair,
    )

    bezier(
        face.x_left_sq,
        face.y_temple,
        face.x_left_sq,
        face.y_hairtop,
        0,
        face.y_hairmid,
        face.x_right_sq,
        face.y_hair,
    )

    bezier(
        face.x_left_sq,
        face.y_hair,
        face.x_left_sq,
        face.y_hairtop,
        0,
        face.y_hairmid,
        face.x_right_eye_end,
        face.y_hair,
    )


def ears(face, cell):

    for e in range(2):
        x_ear_start = face.x_ear_RS if e else face.x_ear_LS
        x_ear_end = face.x_ear_RE if e else face.x_ear_LE
        x_box = face.x_right_sq if e else face.x_left_sq

        pushStyle()
        strokeWeight(4)
        bezier(
            x_ear_start,
            face.y_ear_start,
            x_ear_start,
            face.y_ear_top,
            x_ear_end,
            face.y_ear_top,
            x_ear_start,
            face.y_ear_bottom,
        )

        popStyle()
