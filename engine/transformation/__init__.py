from matrix import Matrix
from math import cos, sin, pi

class Transformation():
    stack = None

    r = {
            "x": [1, 2],
            "y": [2, 0],
            "z": [0, 1],
            }

    def __init__(self, stack):
        self.stack = stack

    def scale(self, sx=1, sy=1, sz=1):
        dilation = Matrix.ident()
        factor = [sx, sy, sz]
        for i in range(3):
            dilation[i][i] = factor[i]
        Matrix.multiply(self.stack[-1], dilation, True)

    def move(self, tx=0, ty=0, tz=0):
        translation = Matrix.ident()
        addend = [tx, ty, tz]
        for i in range(3):
            translation[i][3] = addend[i]
        Matrix.multiply(self.stack[-1], translation, True)
    
    def rotate(self, axis="z", angle=0):
        r = self.r
        angle = angle * pi / 180
        rotation = Matrix.ident()
        rotation[r[axis][0]][r[axis][0]] = cos(angle)
        rotation[r[axis][1]][r[axis][0]] = -sin(angle)
        rotation[r[axis][0]][r[axis][1]] = sin(angle)
        rotation[r[axis][1]][r[axis][1]] = cos(angle)
        Matrix.multiply(self.stack[-1], rotation, True)
