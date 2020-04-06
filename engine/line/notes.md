# Drawing Lines

#### algorithm:
	for x0 -> x1:
		test(x+1, y+1)
		test(x+1, y)
		pick best pixel

	for x0 -> x1:
		v0 = f(x + 1, y + 1)
		v1 = f(x + 1, y)
		if abs(v0) < abs(v1)
			plot(x + 1, y + 1)
		else:
			plot(x + 1, y)

test fxn:
	Ax + B + C = 0
	A = (delta y)
	B = -(delta x)
	C = (delta x) b

use f(x + 1, y + 1/2) and compare that to 0
if positive, the line is above (pick top)
if negative, the line is below (pick bot)

#### new alg:
	for x0 -> x1:
		d = f(x + 1, y + 1/2)
		x += 1
		if d > 0:
			y += 1

		plot(x, y)

###### another thing to note:
f(x0, y0) = 0
f(x0 + 1, y0 + 1/2) = A + 1/2 B

can get rid of fxn

###### Octant 1:
	0 < m < 1
	Possible Points:
		(x+1, y), (x+1, y+1)
	Midpoint:
		(x+1, y+1/2)
	Initial d: A + 1/2B

x = x0
d = 2A + B
while x <= x1:
	plot(x,y)
	if d > 0:
		y += 1
		d += 2B
	x += 1
	d += 2A

###### Octant 2:
	1 < m
	Possible Points: 
		(x,y+1), (x+1,y+1)
	Midpoint:
		(x+1/2, y+1)
	Initial d: 1/2A + B
	flip d
