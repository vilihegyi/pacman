from movement import *


def create_ghosts():
    # Orange ghost - Clyde
    orange_ghost.shape("pictures/Ghost_orange.gif")
    orange_ghost.speed(0)
    orange_ghost.penup()
    orange_ghost.direction = "up"
    orange_ghost.goto(-30, 20)
    orange_ghost.stamp()
    # Pink ghost - Pinky
    pink_ghost.shape("pictures/Ghost_pink.gif")
    pink_ghost.speed(0)
    pink_ghost.penup()
    pink_ghost.direction = "up"
    pink_ghost.goto(-10, 20)
    pink_ghost.stamp()
    # Red ghost - Blinky
    red_ghost.shape("pictures/Ghost_red.gif")
    red_ghost.speed(0)
    red_ghost.penup()
    red_ghost.direction = "up"
    red_ghost.goto(10, 20)
    red_ghost.stamp()
    # Turquoise ghost - Inky
    turquoise_ghost.shape("pictures/Ghost_turquoise.gif")
    turquoise_ghost.speed(0)
    turquoise_ghost.penup()
    turquoise_ghost.direction = "up"
    turquoise_ghost.goto(30, 20)
    turquoise_ghost.stamp()


def move_ghost(ghost):
    x = ghost.xcor()
    y = ghost.ycor()
    if x < get_player().x and movement_is_valid(x + 10, y):
        x += 10
    elif x > get_player().x and movement_is_valid(x - 10, y):
        x -= 10
    elif y < get_player().y and movement_is_valid(x, y + 10):
        y += 10
    elif y >= get_player().y and movement_is_valid(x, y - 10):
        y -= 10

    # Refresh coordinates and reset the direction
    if movement_is_valid(x, y):
        ghost.setx(x)
        ghost.sety(y)


def release_ghosts():
    orange_ghost.clear()
    red_ghost.clear()
    pink_ghost.clear()
    turquoise_ghost.clear()
    orange_ghost.setx(-30)
    orange_ghost.sety(80)
    red_ghost.setx(-10)
    red_ghost.sety(80)
    pink_ghost.setx(10)
    pink_ghost.sety(80)
    turquoise_ghost.setx(30)
    turquoise_ghost.sety(80)


# Ghosts
orange_ghost = turtle.Turtle()
red_ghost = turtle.Turtle()
pink_ghost = turtle.Turtle()
turquoise_ghost = turtle.Turtle()

