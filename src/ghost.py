import random

from movement import *


def create_ghosts():
    orange_ghost.shape("pictures/Ghost_orange.gif")
    orange_ghost.speed(0)
    orange_ghost.penup()
    orange_ghost.direction = "up"
    orange_ghost.goto(-30, 20)
    orange_ghost.stamp()
    pink_ghost.shape("pictures/Ghost_pink.gif")
    pink_ghost.speed(0)
    pink_ghost.penup()
    pink_ghost.direction = "up"
    pink_ghost.goto(-10, 20)
    pink_ghost.stamp()
    red_ghost.shape("pictures/Ghost_red.gif")
    red_ghost.speed(0)
    red_ghost.penup()
    red_ghost.direction = "up"
    red_ghost.goto(10, 20)
    red_ghost.stamp()
    turquoise_ghost.shape("pictures/Ghost_turquoise.gif")
    turquoise_ghost.speed(0)
    turquoise_ghost.penup()
    turquoise_ghost.direction = "up"
    turquoise_ghost.goto(30, 20)
    turquoise_ghost.stamp()


def move_orange_ghost():
    direction = random.randint(0, 4)
    if direction == 1:
        direction_string = "up"
    elif direction == 2:
        direction_string = "down"
    elif direction == 3:
        direction_string = "left"
    else:
        direction_string = "right"
    move_ghost(orange_ghost, direction_string)


def move_red_ghost():
    direction = random.randint(0, 4)
    if direction == 1:
        direction_string = "up"
    elif direction == 2:
        direction_string = "down"
    elif direction == 3:
        direction_string = "left"
    else:
        direction_string = "right"
    move_ghost(red_ghost, direction_string)


def move_pink_ghost():
    direction = random.randint(0, 4)
    if direction == 1:
        direction_string = "up"
    elif direction == 2:
        direction_string = "down"
    elif direction == 3:
        direction_string = "left"
    else:
        direction_string = "right"
    move_ghost(pink_ghost, direction_string)


def move_turquoise_ghost():
    direction = random.randint(0, 4)
    if direction == 1:
        direction_string = "up"
    elif direction == 2:
        direction_string = "down"
    elif direction == 3:
        direction_string = "left"
    else:
        direction_string = "right"
    move_ghost(turquoise_ghost, direction_string)


def move_ghost(ghost, direction):
    x = ghost.xcor()
    y = ghost.ycor()
    if direction == "up" and y < 280:
        y += 10
    if direction == "down" and y > -280:
        y -= 10
    if direction == "left" and x > -250:
        x -= 10
    if direction == "right" and x < 250:
        x += 10
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

