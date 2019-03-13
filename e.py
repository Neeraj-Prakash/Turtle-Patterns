import turtle
t = turtle.Pen()
turtle.bgcolor("midnightblue")
t.speed(0)
#list color
colors = [ "antiquewhite",
           "mediumseagreen",                #Watch the pattern building                          
           "burlywood",
           "dodgerblue"]

for x in range(350):
    t.pencolor( colors[ x % 4] )
    t.forward(2*x)
    t.left(100)
