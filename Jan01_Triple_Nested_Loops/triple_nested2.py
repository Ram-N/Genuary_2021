"""
Created as a sketch for Genuary 2021: https://genuary2021.github.io/prompts
Genuary 2021: Jan 01 Sketch

Triple Nested Loop

Author: Ram Narasimhan
"""

w, h = 840, 840
margin = 20
PRIME = 7


def setup():
    size(w, h)
    background(127)

    pushMatrix()
    translate(width / 2, height / 2)

    for v1 in range(10):
        translate(v1 * width / 15, v1 * height / 8)
        for v2 in range(10):
            for v3 in range(0, 100, 20):
                rotate(PI / PRIME * 10)

                strokeWeight(1 + abs(70 - 1 * v2))
                stroke(180, 2 * v3, 5 * v2, 40)
                line(v2, 80, 10 * v2 + 240, 10 * v2 - 240)

                strokeWeight(3 + abs(7 - 3 * v2))
                stroke(v1 * 20, 150, 10)
                ellipse(v2 * 10, 80, 3 * v2 + 24, 3 * v2 - 24)

                stroke(10)
                ellipse(v2 * 5, v3, 5, 5)

    stroke(200)
    strokeWeight(20)
    noFill()
    rect(0, 0, w - 2 * margin, h - 2 * margin)
    popMatrix()

    stroke(255)
    rect(0, 0, w, h)

    save("images/triple_nested7.png")
