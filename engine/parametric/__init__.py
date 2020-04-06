import math

class Parametric:
    step = -1
    edges = None

    def __init__(self, edgeMatrix, step=0.01):
        self.edges = edgeMatrix
        self.step = step

    def arc(self, center, radius, angle=2*math.pi):
        x = lambda t: center[0] + radius * math.cos(angle * t)
        y = lambda t: center[1] + radius * math.sin(angle * t)
        z = lambda t: center[2]
        self.add(x, y, z)

    def hermite(self, p0, p1, r0, r1):
        f = lambda i: lambda t: (2 * p0[i] - 2 * p1[i] + r0[i] + r1[i]) * t ** 3 + (-3 * p0[i] + 3 * p1[i] - 2 * r0[i] - r1[i]) * t ** 2 + r0[i] * t + p0[i]
        x = f(0)
        y = f(1)
        self.add(x, y)

    def bezier(self, p0, p1, p2, p3):
        f = lambda i: lambda t: (-p0[i] + 3 * p1[i] - 3 * p2[i] + p3[i]) * t ** 3 + (3 * p0[i] - 6 * p1[i] + 3 * p2[i]) * t ** 2 + (-3 * p0[i] + 3 * p1[i]) * t + p0[i]
        x = f(0)
        y = f(1)
        self.add(x, y)

    def add(self, x, y, z=lambda t: 0):
        step = self.step
        t = 0
        while t < 1:
            self.edges.addEdge((x(t), y(t), 0), (x(min(t + step, 1)), y(min(t + step, 1)), 0))
            t += step
