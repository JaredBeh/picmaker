def draw():
    buffer = "P3\n500 500 255\n"
    f = open("image_hw_0.ppm","w+")
    for x in range(500):
        for y in range(500):
            r = (x + y) % 255
            g = (x * y) % 255
            b = (x ^ y) % 255
            buffer+= "%d %d %d " % (r, g, b)
        buffer += "\n"
    f.write(buffer)
draw()
