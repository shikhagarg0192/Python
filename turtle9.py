import turtle
turtle.setup(400,800)

turtle.left(90)
turtle.circle(10,360)

turtle.left(90)
turtle.forward(10)
turtle.right(180)

for i in range(9):
    turtle.left(36)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(180)

'''turtle.forward(50)
'''
turtle.mainloop()
