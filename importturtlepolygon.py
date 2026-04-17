import turtle

polygon = turtle.Turtle()

numofsides = 6
sidelength = 60
angle = 360.0/numofsides

for i in range(numofsides):
    polygon.forward(sidelength)
    polygon.right(angle)

turtle.done()    
