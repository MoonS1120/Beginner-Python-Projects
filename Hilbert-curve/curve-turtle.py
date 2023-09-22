import turtle

WIDTH, HEIGHT = 600, 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

curve = turtle.Turtle()
curve.speed(0)

'''
A = hilbert(turtle, level-1, length, angle)
B = hilbert(turtle, level-1, length, -angle)
F = curve.forward(length)
+ = curve.left(angle)
− = curve.right(angle)

A → +BF−AFA−FB+
B → −AF+BFB+FA−
'''

def hilbert(curve, level, length, angle):
    if level == 0:
        return
    curve.left(angle)
    hilbert(curve, level-1, length, -angle)
    curve.forward(length)
    curve.right(angle)
    hilbert(curve, level-1, length, angle)
    curve.forward(length)
    hilbert(curve, level-1, length, angle)
    curve.right(angle)
    curve.forward(length)
    hilbert(curve, level-1, length, -angle)
    curve.left(angle)

n = 4

hilbert(curve, n, (WIDTH-8)/(2**n-1), 90)
turtle.done()