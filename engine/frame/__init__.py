from math import pi, cos, sin

class Frame:
    edges = None
    step = -1

    def __init__(self, edges, step=0.01):
        self.edges = edges
        self.step = step

    def addPoints(self, x, y, z):
        m = self.edges
        phi = 0
        while phi < 1:
            theta = 0
            while theta < 1:
                m.addEdge((x(theta, phi), y(theta, phi), z(theta, phi)),
                        (x(theta, phi), y(theta, phi), z(theta, phi)))
                theta += self.step
            phi += self.step
    
    def box(self, corner, dim):
        m = self.edges
        m.addEdge(corner, (corner[0] + dim[0], corner[1], corner[2]))
        m.addEdge(corner, (corner[0], corner[1] - dim[1], corner[2]))
        m.addEdge(corner, (corner[0], corner[1], corner[2] - dim[2]))
        m.addEdge((corner[0], corner[1] - dim[1], corner[2] - dim[2]),
                (corner[0], corner[1], corner[2] - dim[2]))
        m.addEdge((corner[0], corner[1] - dim[1], corner[2] - dim[2]),
                (corner[0], corner[1] - dim[1], corner[2]))
        m.addEdge((corner[0], corner[1] - dim[1], corner[2] - dim[2]),
                (corner[0] + dim[0], corner[1] - dim[1], corner[2] - dim[2]))
        m.addEdge((corner[0] + dim[0], corner[1] - dim[1], corner[2]),
                (corner[0], corner[1] - dim[1], corner[2]))
        m.addEdge((corner[0] + dim[0], corner[1] - dim[1], corner[2]),
                (corner[0] + dim[0], corner[1], corner[2]))
        m.addEdge((corner[0] + dim[0], corner[1] - dim[1], corner[2]),
                (corner[0] + dim[0], corner[1] - dim[1], corner[2] - dim[2]))
        m.addEdge((corner[0] + dim[0], corner[1], corner[2] - dim[2]),
                (corner[0], corner[1], corner[2] - dim[2]))
        m.addEdge((corner[0] + dim[0], corner[1], corner[2] - dim[2]),
                (corner[0] + dim[0], corner[1], corner[2]))
        m.addEdge((corner[0] + dim[0], corner[1], corner[2] - dim[2]),
                (corner[0] + dim[0], corner[1] - dim[1], corner[2] - dim[2]))

    def sphere(self, center, radius):
        x = lambda theta, phi: radius * cos(theta * 2 * pi) + center[0]
        y = lambda theta, phi: radius * sin(theta * 2 * pi) * cos(phi * pi) + center[1]
        z = lambda theta, phi: radius * sin(theta * 2 * pi) * sin(phi * pi) + center[2]
        self.addPoints(x, y, z)

    def torus(self, center, radius1, radius2):
        x = lambda theta, phi: cos(phi * 2 * pi) * (radius1 * cos(theta * 2 * pi) + radius2) + center[0]
        y = lambda theta, phi: radius1 * sin(theta * 2 * pi) + center[1]
        z = lambda theta, phi: - sin(phi * 2 * pi) * (radius1 * cos(theta * 2 * pi) + radius2) + center[2]
        self.addPoints(x, y, z)
