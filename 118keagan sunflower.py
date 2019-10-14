#   a113_flower_2x_petals.py
#   This code draws a flower with 9-10 petals
import turtle as trtl

drawer = trtl.Turtle()
drawer.speed(0)


#this code will draw the stem i am looking for
drawer.color("green")
drawer.pensize(10)
drawer.goto(0,-170)
#this is where the code for my bottom leaf is
drawer.setheading(90)
drawer.forward(120)
drawer.circle(20, 120, 20)
drawer.setheading(90)
drawer.goto(0, (drawer.ycor()-10))
drawer.forward(110)
#this is where the code for the top leaf will go
drawer.setheading(270)
drawer.circle(20, 120, 20)
drawer.setheading(90)
drawer.goto(0, (drawer.ycor()+10))
#stem forward
drawer.forward(60)
drawer.goto(0,180)
drawer.setheading(0)
drawer.fillcolor("black")
drawer.begin_fill()
drawer.circle(90)
drawer.end_fill()

drawer.up()
drawer.goto(0,275)
drawer.shape("circle")
drawer.color("yellow")
petals = 20
while (petals < 40):
    drawer.right(20)
    drawer.forward(80)
    drawer.pendown()
    drawer.circle(8)
    drawer.penup()
    drawer.goto(0,275)
    petals = petals + 1



















wn = trtl.Screen()
wn.mainloop()