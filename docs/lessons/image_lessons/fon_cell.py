from turtle import *

def fon(CELL_SIZE=40):
    tracer(0)
    screen = Screen()
    # Повноекранний режим
    screen.setup(width=1.0, height=1.0)

    WIDTH = screen.window_width()
    HEIGHT = screen.window_height()

    screen.bgcolor("white")
   
    grid = Turtle()
    grid.hideturtle()
    grid.speed(0)
    grid.color("#cccccc")
    grid.pensize(1)

    left = -WIDTH // 2
    right = WIDTH // 2
    bottom = -HEIGHT // 2
    top = HEIGHT // 2

    # --- Вертикальні лінії ---
    x = 0
    while x <= right:
        grid.penup()
        grid.goto(x, bottom)
        grid.pendown()
        grid.goto(x, top)

        if x != 0:
            grid.penup()
            grid.goto(-x, bottom)
            grid.pendown()
            grid.goto(-x, top)

        x += CELL_SIZE

    # --- Горизонтальні лінії ---
    y = 0
    while y <= top:
        grid.penup()
        grid.goto(left, y)
        grid.pendown()
        grid.goto(right, y)

        if y != 0:
            grid.penup()
            grid.goto(left, -y)
            grid.pendown()
            grid.goto(right, -y)

        y += CELL_SIZE

    # --- Осі ---
    axis = Turtle()
    axis.hideturtle()
    axis.speed(0)
    axis.pensize(2)
    axis.color("black")

    axis.penup()
    axis.goto(left, 0)
    axis.pendown()
    axis.goto(right, 0)

    axis.penup()
    axis.goto(0, bottom)
    axis.pendown()
    axis.goto(0, top)
    update()
    tracer(True)
