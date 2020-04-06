# 3D Shapes
- Box
- Sphere
- Torus

### Box
Given information:
- vertex (front-top-left)
- width
- depth
- height
Defining points:
- 8 vertices
Add 12 edges

### Sphere
Given information:
- center
- radius
Defining points:
- Points on the surface
- Circles drawn on the surface (Longitude Lines)
  - x = r cos(theta) + cx
  - y = r sin(theta) cos(phi) + cy
  - z = r sin(theta) sin(phi) + cz
  - theta: 0 - 2 * pi
  - phi: 0 - pi

### Torus
Given information:
- center
- radius of cross section
- distance from torus center to cross section center
Defining points:
- Points on the surface
- Circles drawn on the surface
  - x = cos(phi) (r cos(theta) + R) + cx
  - y = r sin(theta) + cy
  - z = -sin(phi) (r cos(theta) + R) + cz
