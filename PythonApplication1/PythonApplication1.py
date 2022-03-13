import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flags")
screen.screensize(120, 100)

wop = turtle.Turtle()

wop.shape("turtle")

wop.up()
wop.goto(-350, 200)
wop.down()

wop.color("blue")
wop.speed(20)

for i in range(100):
    wop.fd(700)
    wop.rt(90)
    wop.fd(1)
    wop.rt(90)
    wop.fd(700)
    wop.lt(90)
    wop.fd(1)
    wop.lt(90)

wop.color("yellow")
for i in range(100):
    wop.fd(700)
    wop.rt(90)
    wop.fd(1)
    wop.rt(90)
    wop.fd(700)
    wop.lt(90)
    wop.fd(1)
    wop.lt(90)

wop.fd(700)

def write(message, pos, color, size):
    x, y = pos
    wop.color(color)
    wop.penup()
    wop.goto(x, y)
    wop.pendown()
    style = ('Arial', size, 'italic')
    wop.write(message, font=style)

write('Ukraine',
      (-200, 200), 'white', 80)
write('#STAND WITH UKRAINE',
      (-300, -300), 'white', 40)

wop.hideturtle()

turtle.mainloop()
