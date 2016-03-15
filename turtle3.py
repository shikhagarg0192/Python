import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(1)
tess.shape("triangle")

def h1(x, y):
   wn.title("Got click at coords {0}, {1}".format(x, y))
   tess.goto(x, y)

wn.onclick(h1)  # Wire up a click on the window.
turtle.mainloop()
