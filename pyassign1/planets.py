import turtle,math  
sun=turtle.Turtle()  
sun.dot(19,'yellow')  
sun.hideturtle()  
mercury=turtle.Turtle()  
venus=turtle.Turtle()  
earth=turtle.Turtle()  
mars=turtle.Turtle()  
jupyter=turtle.Turtle()  
saturn=turtle.Turtle()  
pl=[mercury,venus,earth,mars,jupyter,saturn]  
co=['blue','green','black','red','orange','lightblue']  
i=[1,2,3,4,5,6]  
def planets(planet,color,i):  
    planet.speed(0)  
    planet.penup()  
    planet.setx(78*i-58)  
    planet.pendown()  
    planet.color(color,color)  
    planet.shape('circle')  
    planet.shapesize((i+1)/5)  
for j in range(6):  
    planets(pl[j],co[j],i[j])  
a=[16,89,171,237,312,380]  
b=[4,9,5,17,20,30]  
c=[14,80,146,220,290,360]  
d=[5,2,1,1/1.5,1/2.4,1/3.3]  
for t in range(100000):  
    for u in range(6):  
        pl[u].goto(a[u]*math.cos(math.radians(d[u]*t))+b[u],c[u]*math.sin(math.radians(d[u]*t)))  
