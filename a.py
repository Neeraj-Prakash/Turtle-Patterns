import turtle                                   #import turtle
import time
t = turtle.Pen()
turtle.bgcolor("cyan")                          #Some unimportant Code                    
t.speed(0) 
t.width(2)
t.pencolor("magenta")

for x in range(17):
    t.circle(100) 
    t.left(42)
    time.sleep(0.5)
