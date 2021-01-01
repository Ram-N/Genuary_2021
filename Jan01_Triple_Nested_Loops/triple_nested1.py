"""
Created as a sketch for Genuary 2021: https://genuary2021.github.io/prompts
"""

w, h = 840, 840
margin = 20


def setup():
    size(w, h)
    background(127)

    pushMatrix()
    #    fill(255)
    # rect(margin, margin, w - 2 * margin, h - 2 * margin)
    translate(width / 2, height / 2)

    for v3 in range(10):
        translate(v3 * width / 15, v3 * height / 8)
        for v1 in range(10):
            for v2 in range(0, 100, 20):
                rotate(PI / 7 * 10)

                strokeWeight(1 + abs(70 - 1 * v1))
                stroke(150, v2, 10 * v1, 60)
                line(v1, 80, 10 * v1 + 240, 10 * v1 - 240)

                strokeWeight(3 + abs(7 - 3 * v1))
                stroke(v3 * 20, 150, 100)
                ellipse(v1 * 10, 80, 3 * v1 + 24, 3 * v1 - 24)

                stroke(10)
                ellipse(v1 * 5, v2, 5, 5)

    stroke(200)
    strokeWeight(20)
    noFill()
    rect(0, 0, w - 2 * margin, h - 2 * margin)
    popMatrix()

    stroke(255)
    rect(0, 0, w, h)


# def draw():
