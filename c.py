import turtle
t = turtle.Pen()
turtle.bgcolor("tomato")
t.speed(0)
colors = ["blueviolet",
          "darkgreen",
          "cornflowerblue",     
          "maroon"]                                 #Some unImportant code                     

for x in range(230):
    t.pencolor( colors[ x % 4] )
    t.circle(x)
    t.left(90)
