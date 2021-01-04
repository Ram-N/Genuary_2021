"""

Created for Genuary2021.
Something human.

Author: Ram Narasimhan

"""


class Face(object):
    def __init__(self, _cx, _cy, _radius, cell):
        self.cx, self.cy = _cx, _cy  # face center, 0,0
        self.radius = _radius

        self.x_left_sq = cell.gw * -4
        self.x_right_sq = cell.gw * 4

        self.y_top_sq = _radius * sin(-PI / 4)
        self.y_bottom_sq = _radius * sin(3 * PI / 4)
        self.sq_cell = (self.x_right_sq - self.x_left_sq) / 2.0
        self.box_len = self.x_right_sq - self.x_left_sq

        # EYES
        self.eye_len = 2 * cell.gw
        self.x_left_eye_end, self.x_left_eye_start = cell.gw * -3, -cell.gw
        self.x_right_eye_end, self.x_right_eye_start = cell.gw * 3, cell.gw

        self.x_left_brow_end, self.x_left_brow_start = cell.gw * -3, -cell.gw
        self.x_right_brow_end, self.x_right_brow_start = cell.gw * 3, cell.gw

        self.y_hairtop = -5 * cell.gh
        self.y_hairmid = -4 * cell.gh
        self.y_hair = -3 * cell.gh
        self.y_brow = -cell.gh
        self.y_ear_top = -cell.gh
        self.y_ear_start = 0
        self.eye_upper = -0.5 * cell.gh
        self.y_eyeline = 0
        self.eye_lower = 0.5 * cell.gh
        self.y_nose = 2 * cell.gh

        self.y_ear_bottom = 2 * cell.gh
        self.y_upper_lip = 2 * cell.gh
        self.y_mouth = 2.5 * cell.gh
        self.y_lower_lip = 3 * cell.gh

        self.y_chintip = 5 * cell.gh

        self.x_mouth_L, self.x_mouth_R = -self.eye_len, self.eye_len

        self.x_ear_LS, self.x_ear_RS = cell.gw * -4, cell.gw * 4
        self.x_ear_LE, self.x_ear_RE = cell.gw * -5.5, cell.gw * 5.5

        ellipse(0, 0, 5, 5)

    def draw_face(self, cell):

        outline(self)
        eyes(self, cell)
        hair(self)
        ears(self, cell)
        mouth(self, cell)

    def eye_brows(self, cell):
        pushStyle()
        strokeWeight(4)
        noFill()
        radian_margin = 0.4
        brow_radius = 10 + int(random(40))
        bezier(
            self.x_right_brow_end,
            self.y_brow,
            self.x_right_brow_end * 1.3,
            self.y_brow - cell.gh * 0.5,
            self.x_right_brow_end * 0.7,
            self.y_brow - cell.gh * 0.5,
            self.x_right_brow_start,
            self.y_brow,
        )

        bezier(
            self.x_left_brow_end,
            self.y_brow,
            self.x_left_brow_end * 1.3,
            self.y_brow - cell.gh * 0.5,
            self.x_left_brow_end * 0.7,
            self.y_brow - cell.gh * 0.5,
            self.x_left_brow_start,
            self.y_brow,
        )

        # ellipse(self.x_right_eye_start + self.eye_len, self.y_brow, 5, 5)
        popStyle()


def hair_line(self):

    line(self.x_left_sq, self.y_hair, self.x_right_sq, self.y_hair)  # hair box top


def nose_line(face):
    pushStyle()
    strokeWeight(3)
    line(face.x_left_eye_start, face.y_nose, face.x_right_eye_start, face.y_nose)

    popStyle()


def draw_sides(face):
    color(200)
    noFill()
    line(face.x_left_sq, face.y_hair, face.x_left_sq, face.y_nose)
    line(face.x_right_sq, face.y_hair, face.x_right_sq, face.y_nose)


def outline(face):

    draw_sides(face)
    nose_line(face)
    chin(face)


def chin(face):
    # bezier from rt_nose to chintip
    # bezier from left_nose to chintip
    chin_dist = face.y_chintip - face.y_nose
    bezier(
        face.x_left_sq,
        face.y_nose,
        face.x_left_sq * 0.7,
        face.y_nose + chin_dist * 0.7,
        face.x_left_sq * 0.5,
        face.y_nose + chin_dist * 0.5,
        0,
        face.y_chintip,
    )

    bezier(
        face.x_right_sq,
        face.y_nose,
        face.x_right_sq * 0.7,
        face.y_nose + chin_dist * 0.7,
        face.x_right_sq * 0.5,
        face.y_nose + chin_dist * 0.5,
        0,
        face.y_chintip,
    )


def eyes(face, cell):
    face.eye_brows(cell)

    # line(face.x_right_eye_end, face.y_eyeline, face.x_right_eye_start, face.y_eyeline)
    # line(face.x_left_eye_end, face.y_eyeline, face.x_left_eye_start, face.y_eyeline)

    pushStyle()
    strokeWeight(3)

    for e in range(2):
        x_EE = face.x_left_eye_end if e else face.x_right_eye_end
        x_ES = face.x_left_eye_start if e else face.x_right_eye_start

        x_eye_center = x_ES + (x_EE - x_ES) / 3
        ellipse(x_eye_center, face.y_eyeline, cell.gh / 2, cell.gw / 2)

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
    line(face.x_mouth_L, face.y_mouth, face.x_mouth_R, face.y_mouth)

    for e in range(2):
        x_mouth = face.x_mouth_L if e else face.x_mouth_R

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
        face.y_hair,
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

