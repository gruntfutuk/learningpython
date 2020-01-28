from turtle import *
def scwer(l):
    circle(l)
    left(45)
def draw(l, col, num):
    speed(200)
    color(col)
    width(2)
    for i in range(int(360/num)):
        color(col)
        scwer(l)
        color("red")
        scwer(l)
        left(num)
draw(100, "blue", 4)
draw(120, "white", 5)
