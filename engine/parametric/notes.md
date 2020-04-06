# Parametric Equations
- Define curves as systems of equations in terms of a single variable

# Splines
- Curves (Cubic) that can be connected to appear smooth/continuous
- Bezier and Hermite Curves

### Bezier Curves
- Defined by 4 control points: 2 endpoints and 2 influence curves
##### Quadratic
- Points are parametrically defined on the line connecting the adjacent points
- The lines are connected, and a point is picked parametrically on the curve
- This creates a moving endpoint
- (1-t)^2P0 + 2t(1-t)P1 + t^2P2
##### Cubic
- By extrapolation, (1-t)^3P0 + 3(1-t)^2tP1 + 3(1-t)t^2P2 + t^3P3
- Getting the polynomial in terms of t yields (-P0 + 3P1 - 3P2 + P3)t^3 + (3P0 - 6P1 + 3P2)t^2 + (-3P0 + 3P1)t + P0

### Hermite Curves
Defined by
- 2 Endpoints
- Rates of Change at each endpoint
| 2 | -2 | 1 | 1 |
| -3 | 3 | -2 | -1 |
| 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 |
- (2P0 - 2P1 + R0 + R1)t^3 + (-3P0 + 3P1 -2R0 - R1)t^2 + (R0)t + P0
