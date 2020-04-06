from math import sin, cos, pi

class Polygon:
    matrix = None
    step = -1

    def __init__(self, matrix, step=0.05, view=(0, 0, 1)):
        self.matrix = matrix
        self.step = step
        self.view = view

    def addPoints(self, points, x, y, z):
        phi = 0
        while phi < 1:
            theta = 0;
            circ = [];
            while theta < 1:
                circ.append((x(theta, phi), y(theta, phi), z(theta, phi)))
                theta += self.step
            if theta > 1:
                circ.append((x(1, phi), y(1, phi), z(1, phi)))
            points.append(circ)
            phi += self.step

    def box(self, corner, dim):
        m = self.matrix
        coord = (corner[0] + dim[0], corner[1] - dim[1], corner[2] - dim[2])
        p = [
                corner,
                (corner[0], coord[1], corner[2]),
                (coord[0], coord[1], corner[2]),
                (coord[0], corner[1], corner[2]),
                (coord[0], corner[1], coord[2]),
                (coord[0], coord[1], coord[2]),
                (corner[0], coord[1], coord[2]),
                (corner[0], corner[1], coord[2]),
                ]
        m.addPolygon(p[0], p[1], p[2])
        m.addPolygon(p[2], p[3], p[0])
        m.addPolygon(p[4], p[5], p[6])
        m.addPolygon(p[6], p[7], p[4])
        m.addPolygon(p[0], p[3], p[4])
        m.addPolygon(p[4], p[7], p[0])
        m.addPolygon(p[1], p[6], p[5])
        m.addPolygon(p[5], p[2], p[1])
        m.addPolygon(p[4], p[3], p[2])
        m.addPolygon(p[2], p[5], p[4])
        m.addPolygon(p[0], p[7], p[6])
        m.addPolygon(p[6], p[1], p[0])

    def sphere(self, center, radius):
        m = self.matrix
        p = []
        x = lambda theta, phi: radius * cos(theta * pi) + center[0]
        y = lambda theta, phi: radius * sin(theta * pi) * cos(phi * 2 * pi) + center[1]
        z = lambda theta, phi: radius * sin(theta * pi) * sin(phi * 2 * pi) + center[2]
        self.addPoints(p, x, y, z)
        a = len(p)
        for i in range(a):
            for j in range(len(p[i])):
                try:
                    m.addPolygon(p[i][j], p[(i + 1) % a][j], p[(i + 1) % a][j + 1])
                    m.addPolygon(p[i][j], p[(i + 1) % a][j + 1], p[i][j + 1])
                except IndexError:
                    pass


    def torus(self, center, radius1, radius2):
        m = self.matrix
        p = []
        x = lambda theta, phi: cos(phi * 2 * pi) * (radius1 * cos(theta * 2 * pi) + radius2) + center[0]
        y = lambda theta, phi: radius1 * sin(theta * 2 * pi) + center[1]
        z = lambda theta, phi: - sin(phi * 2 * pi) * (radius1 * cos(theta * 2 * pi) + radius2) + center[2]
        self.addPoints(p, x, y, z)
        a = len(p)
        for i in range(a):
            for j in range(len(p[i])):
                try:
                    m.addPolygon(p[i][j], p[(i + 1) % a][j], p[(i + 1) % a][j + 1])
                    m.addPolygon(p[i][j], p[(i + 1) % a][j + 1], p[i][j + 1])
                except IndexError:
                    pass

    def normal(p0, p1, p2):
        v0 = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])
        v1 = (p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2])
        return (
                v0[1] * v1[2] - v0[2] * v1[1],
                v0[2] * v1[0] - v0[0] * v1[2],
                v0[0] * v1[1] - v0[1] * v1[0]
                )
