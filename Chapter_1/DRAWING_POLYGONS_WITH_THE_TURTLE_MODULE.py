from turtle import *


def square(sidelength = 100):
    for i in range(4):
        forward(sidelength)
        right(90)
    right(5)


def triangle(sidelength = 100):
    for i in range(3):
        forward(sidelength)
        right(120)


def polygon(sides):
    for _ in range(sides):
        forward(100)
        right(360 / sides)


def spiral(sidelength = 100):
    for i in range(4):
        forward(sidelength)
        right(90)
    right(5)


def star():
    for i in range(5):
        forward(150)
        right(144)

def star_spiral(sidelength=100):
    for i in range(5):
        forward(sidelength)
        right(144)
    right(5)


shape('turtle')

#Polygon

# polygon(4)

# Spiral of squares

# length = 5
# for i in range(60):
#     spiral(length)
#     length += 5

# Star spiral

#star()

length = 5

for i in range(60):
    star_spiral(length)
    length += 5