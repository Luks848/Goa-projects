from turtle import*

#we want to paint a house

#step 1: draw a square
width(7)
begin_fill()
color("green")
forward(200)
left(90)
end_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
begin_fill()
color("red")
left(90)
forward(100) #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(10,120)
pendown()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
penup()
goto(10,145)
pendown()
right(90)
forward(50)
penup()
goto(140,120)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
goto(165, 120)
left(180)
forward(50)
penup()
goto(140, 145)
pendown()
right(90)
forward(50)


exitonclick()



