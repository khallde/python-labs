import turtle

penColor = input("Enter a pen color: ").lower()

userInput = 1

turtle.color(penColor)

while userInput != 0:
    userInput = int(input("Enter your next move:"))
    turtle.forward(userInput * 10)
