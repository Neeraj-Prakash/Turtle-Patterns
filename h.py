import turtle
t = turtle.Pen()
t.speed(0)
sides = int(turtle.numinput("How many sides in your work my friend?",
"How many sides do you want, gave one number?", 4))

for m in range(5,100): 
    t.left(360/sides + 2)
    t.width(m//25+1)
    t.penup() 
    t.forward(m*4) 
    t.pendown()
                                                        # Watch The Pattern                        
    if (m % 2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)
