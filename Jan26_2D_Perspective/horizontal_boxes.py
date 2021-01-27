def setup():
    size(640, 360, P3D)

    lights()
    fill(50, 60, 200)

    fov = PI / 3.0
    cameraZ = (height / 2.0) / tan(fov / 2.0)
    perspective(fov, float(width) / float(height), cameraZ / 2.0, cameraZ * 2.0)

    # pushMatrix()
    # rotateX(PI / 4)
    # rect(200, height / 2, 300, height / 2)
    # popMatrix()

    for b in range(7):
        pushMatrix()
        translate(80 * (b + 1), height / 2, 0)
        rotateY(-PI + TWO_PI / 7 * b)  # around the vertical Y axis
        # rotateY(PI / 4)
        box(80, 200, 40)
        popMatrix()
