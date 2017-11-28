import turtle
import math
def sin(x):
    y=math.sin(x)
    return y
def cos(x):
    y=math.cos(x)
    return y

wn=turtle.Screen()
wn.screensize(5000,5000)
turtle.bgcolor("black")
sun=turtle.Turtle()
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
e=turtle.Turtle()
f=turtle.Turtle()
g=turtle.Turtle()
h=turtle.Turtle()

sun.color("red")
a.color("gray")
b.color("yellow")
c.color("blue")
d.color("red")
e.color("brown")
f.color("yellow")
g.color("blue")
h.color("lightblue")


sun.shapesize(5)
a.shapesize(0.1)
b.shapesize(0.2)
c.shapesize(0.2)
d.shapesize(0.15)
f.shapesize(0.5)
e.shapesize(0.4)
g.shapesize(0.3)
h.shapesize(0.3)
sun.shape("circle")
for i in [a,b,c,d,e,f,g,h]:
    i.shape("circle")

for i in [a,b,c,d,e,f,g,h]:
    i.penup()
    i.speed(0)
a.setpos(90,0)
b.setpos(150,0)
c.setpos(220,0)
d.setpos(300,0)
e.setpos(600,0)
f.setpos(1000,0)
g.setpos(1500,0)
h.setpos(2000,0)

for i in [a,b,c,d,e,f,g,h]:
    i.pendown()

a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0

for i in range(5000):
    a.setpos(100*cos(a1)-10,95*sin(a1))
    a1=a1+0.07
    b.setpos(155*cos(a2)-5,140*sin(a2))
    a2=a2+0.02
    c.setpos(233*cos(a3)-13,250*sin(a3))
    a3=a3+0.015
    d.setpos(305*cos(a4)-5,310*sin(a4))
    a4=a4+0.01
    e.setpos(666*cos(a5)-66,602*sin(a5))
    a5=a5+0.001
    f.setpos(1080*cos(a6)-80,1111*sin(a6))
    a6=a6+0.0009
    g.setpos(1400*cos(a7)+100,1600*sin(a7))
    a7=a7+0.0005
    h.setpos(1999*cos(a8)+1,2017*sin(a8))
    a8=a8+0.0001
             
    

