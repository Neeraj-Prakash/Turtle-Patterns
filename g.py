import turtle

t = turtle.Pen()
turtle.bgcolor("midnightblue")
t.speed(0)
sides = 4
colors = ["antiquewhite",
          "burlywood",
          "dodgerblue",
          "lime",
          "indianred",
          "mediumslateblue"]
                                                #This one's lit...                               
for x in range(298):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
