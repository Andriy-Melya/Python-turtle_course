from turtle import *
from fon_cell import fon
k = 50
fon(k)
speed(1)
color('blue')
pensize(5)
speed(5)

x = 4 * k
y = 5 * k
penup()
goto(x, y)
pendown()
goto(x - 3 * k, y - 9 * k)
goto(x + 4 * k, y - 3 * k)
goto(x - 4 * k, y - 3 * k)
goto(x + 3 * k, y - 9 * k)
goto(x, y)
goto(x - 4 * k, y - 3 * k)
goto(x - 3 * k, y - 9 * k)
goto(x + 3 * k, y - 9 * k)
goto(x + 4 * k, y - 3 * k)
goto(x, y)





#hideturtle()
done()