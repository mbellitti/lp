from swampy.TurtleWorld import *
from math import pi, sin
from numpy import deg2rad


def polygon(turtle, n, side):
    """takes a turle and draws an n-sided polygon of side side"""
    for x in xrange(n):
        fd(turtle, side)
        lt(turtle, 360./n)


def circle(turtle, r, segments):
    polygon(turtle, segments, 2*pi*r/segments)


def sector(turtle, radius, steps, angle):
    fd(turtle, radius)
    lt(turtle, 90)
    for x in xrange(steps):
        fd(turtle, (float(angle)/steps)*(radius*pi/180.))
        lt(turtle, float(angle)/steps)
    lt(turtle, 90)
    fd(turtle, radius)


def arc(turtle, radius, angle, steps):
    for x in xrange(steps):
        fd(turtle, (float(angle)/steps)*(radius*pi/180.))
        lt(turtle, float(angle)/steps)


def koch(turtle, length):
    if length < 3:
        fd(turtle, length)
    else:
        koch(turtle, length/3.)
        lt(turtle, 60)
        koch(turtle, length/3.)
        rt(turtle, 120)
        koch(turtle, length/3.)
        lt(turtle, 60)
        koch(turtle, length/3.)


def flower(turtle, num, size):
    def petal():
        arc(turtle, size/2./sin(deg2rad(360./num)/2.), 360./num, 100)
        lt(turtle, 180-360./num)
        arc(turtle, size/2./sin(deg2rad(360./num)/2.), 360./num, 100)
    for x in xrange(num):
        petal()
        rt(turtle, 180)
        #lt(turtle, 360./num)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.005

print(bob)

#sides = int(raw_input("Number of sides: "))
#lenght = int(raw_input("Lenght of side: "))

#wait_for_user()
