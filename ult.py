import turtle
from turtle import Screen, Turtle
import math
import time

turtle.tracer(0)
t = Turtle()
s = Screen()
t.width(2)
s.bgcolor("burlywood")                   # The MasterPiece                                                                                     
colors = ["mediumblue", "orange",
          "black", "orangered"]
t.setundobuffer(100)


for i in range(1000):

	t.clear()
	time.sleep(0.05)
	

	t.goto(0,0)
	t.pendown()
	for x in range(100):
		t.pencolor( colors[ x % 4] )
		t.forward(x*2)
		t.left(100+10*math.sin(i/50))		
	t.penup()
	s.update()

	#for y in range(10):
		#t.undo()

#wait = input("PRESS ENTER TO CONTINUE.")
