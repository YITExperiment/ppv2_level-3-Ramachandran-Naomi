import turtle as t
def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('slow')
    t.bgcolor('Black')
#feet
t.goto(-100, -150)
rectangle(50,20,'Aquamarine')
t.goto(-30,-150)
rectangle(50,20,'Aquamarine')
#legs
t.goto(-25, -50)
rectangle(15,100,'Lemon Chiffon')
t.goto(-55,-50)
rectangle(-15,100,'Lemon Chiffon')
#body
t.goto(-90,100)
rectangle(100,150,'Deep pink')
#arms
t.goto(-150, 70)
rectangle(60,15,'Misty Rose')
t.goto(-150,110)
rectangle(15,40,'Misty Rose')

t.goto(10, 70)
rectangle(60,15,'Misty Rose')
t.goto(55,110)
rectangle(15,40,'Misty Rose')
#neck
t.goto(-50,120)
rectangle(15,20,'Aquamarine')
#head
t.goto(-85,160)
rectangle(80,50,'Peach Puff')
#eyes
t.goto(-60,160)
rectangle(30,10,'white')
t.goto(-55,155)
rectangle(5,5,'black')
t.goto(-40,155)
rectangle(5,5,'black')
#mouth
t.goto(-65,135)
rectangle(40,5,'black')

t.hideturtle()

    
    
