from canvas import Picture, Color
from parser import parse

pic = Picture('pic.ppm')
color = pic.addcolor(
        Color(lambda x,y:255,
        lambda x,y:255,
        lambda x,y:255)
        )

parse('script', pic, color)
