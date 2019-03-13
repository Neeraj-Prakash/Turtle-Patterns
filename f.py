import turtle
t = turtle.Pen()
turtle.bgcolor("ivory")
t.speed(0)
colors = ["blueviolet",
          "darkgreen",
          "cornflowerblue",
          "maroon"]
                                                    # Watch The Pattern                         
for x in range(230):
    t.pencolor( colors[ x % 4] )
    t.circle(x)
    t.left(91)
