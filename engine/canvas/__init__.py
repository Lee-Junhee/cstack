from canvas.exceptions import OutOfBoundsException
import subprocess

class Picture:
    fname = ''
    width = -1
    height = -1
    depth = -1
    pixels = list()
    colors = dict()

    def __init__(self, fname, width=500, height=500, depth=255):
        self.colors['background'] = Color(
                lambda x, y: 0,
                lambda x, y: 0,
                lambda x, y: 0
                )
        self.fname = fname
        self.width = width
        self.height = height
        self.depth = depth
        for x in range(height):
            for y in range(width):
                self.pixels += [Pixel(x, y, self.colors['background'])]

    def set(self, x, y, color):
        if -1 < x < self.width:
            if -1 < y < self.height:
                try:
                    self.pixels[self.width * (self.height - y) + x].color = self.colors[color]
                except IndexError:
                    pass
            else:
                raise OutOfBoundsException(f'given y-coordinate {y} does not exist in the picture')
        else:
            raise OutOfBoundsException(f'given x-coordinate {x} does not exist in the picture')

    def addcolor(self, color):
        key = len(self.colors.keys())
        self.colors[key] = color
        return key 

    def clear(self):
        for pixel in self.pixels:
            pixel.color = self.colors['background']

    def display(self):
        self.commit()
        subprocess.run(['display', self.fname])
        subprocess.run(['rm', self.fname])

    def commit(self):
        with open(self.fname, 'w+') as pic:
            pic.write('P3\n')
            pic.write("{width} {height}\n".format(width=self.width, height=self.height))
            pic.write("{depth}\n".format(depth=self.depth))
            for pixel in self.pixels:
                pic.write(pixel.value())
                pic.write("\n")

class Pixel:
    x = -1
    y = -1
    color = None

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def value(self):
        color = self.color.value()
        return "%d %d %d" % (color[0](self.x, self.y), color[1](self.x, self.y), color[2](self.x, self.y))

class Color:
    r = lambda x,y: -1
    g = lambda x,y: -1
    b = lambda x,y: -1

    def __init__(self, r, g, b):
        self.setcolor(r, g, b)

    def setcolor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def value(self):
        return (self.r, self.g, self.b)
