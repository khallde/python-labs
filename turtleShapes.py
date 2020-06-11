import turtle

shapeSides = int(input("How many sides would you like your shape to have? "))

turnAngle = 360 / shapeSides
movementCount = 150

for steps in range(shapeSides):
    for steps in range(shapeSides):
        turtle.right(turnAngle)
        turtle.forward(movementCount)
    movementCount -= (movementCount/shapeSides)
    turtle.penup()
    turtle.left(turnAngle / 2)
    turtle.backward(movementCount/shapeSides)
    turtle.right(turnAngle / 2)
    turtle.pendown()

turtle.done()
