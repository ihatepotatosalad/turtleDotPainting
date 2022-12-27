from turtle import Turtle, Screen, colormode
import random
colormode(255)
colors = [(215, 43, 55), (247, 241, 110),
          (37, 25, 15), (186, 52, 63), (32, 4, 7)]
timmy = Turtle()
timmy.speed(0)
timmy.hideturtle()
timmy.penup()
screen = Screen()


def random_color(list):
    choices = random.choice(list)
    r = choices[0]
    g = choices[1]
    b = choices[2]
    return (r, g, b)


x = -400
y = -300


starting = timmy.setposition(-400, -300)
for j in range(10):
    for i in range(10):
        timmy.pencolor(random_color(colors))
        timmy.dot(20)
        timmy.forward(50)
    y += 50
    timmy.goto(x, y)

    print(timmy.position())

screen.exitonclick()
