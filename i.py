import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

my_turtle.color('red')
                                    #Some Rectangles
guru = turtle.Screen()
guru.bgcolor("orange")

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

for i in range(250): 
        square(150, 90)
        my_turtle.right(11)
