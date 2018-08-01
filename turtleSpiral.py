import turtle


def main():
    window = turtle.Screen()
    window.bgcolor("yellow")
    b = turtle.Turtle()
    b.speed(10)
    b.width(width=1)
    b.shape('turtle')
    b.color('gray')
    d = 5
    angle = 145
    for x in range(1, 580):
        y = 5 if x % 2 == 0 else 8
        col = "red" if x % 2 == 0 else "purple"
        b.color(col)
        b.forward(d)
        b.left(angle)
        b.circle(40 + d / 7)
        d -= 4
    window.exitonclick()


main()
