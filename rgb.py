import turtle
import colorsys
import time

t= turtle.Pen()
turtle.bgcolor('purple')
t.speed(0)
t.width(3)
circles = [25,50,100,200]
flag = 1
time.sleep(2)

for no_of_circles in circles:
    for x in range(no_of_circles):
        
        t.pencolor(colorsys.hsv_to_rgb(x / no_of_circles,1,1))                  # The RGB Wheel                           
        if flag == 1:
            time.sleep(3)
            flag+=1
        t.circle(150)
        t.left(360/no_of_circles)
    time.sleep(2)
    turtle.bgcolor('purple')
