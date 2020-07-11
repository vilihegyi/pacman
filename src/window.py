import time

from movement import *
from player import *


def init_game():
    _window.title("PACMAN in Python")
    _window.bgpic("pictures/background.png")
    _window.bgcolor("black")
    _window.setup(width=560, height=620)
    _window.tracer(0)
    # Keyboard binding for the keys
    _window.listen()
    _window.onkeypress(go_up, "Up")
    _window.onkeypress(go_down, "Down")
    _window.onkeypress(go_right, "Right")
    _window.onkeypress(go_left, "Left")
    _window.onkeypress(go_up, "w")
    _window.onkeypress(go_down, "s")
    _window.onkeypress(go_right, "d")
    _window.onkeypress(go_left, "a")
    # Register the shapes
    _window.register_shape("pictures/Pacman_up.gif")
    _window.register_shape("pictures/Pacman_down.gif")
    _window.register_shape("pictures/Pacman_left.gif")
    _window.register_shape("pictures/Pacman_right.gif")
    _window.register_shape("pictures/Ghost_orange.gif")
    _window.register_shape("pictures/Ghost_pink.gif")
    _window.register_shape("pictures/Ghost_red.gif")
    _window.register_shape("pictures/Ghost_turquoise.gif")


def end_game():
    # Display end message on window
    _pen = turtle.Turtle()
    _pen.hideturtle()
    _pen.speed(0)
    _pen.shape("square")
    _pen.color("white")
    _pen.penup()
    _pen.goto(0, 20)
    _pen.write("Game over!".format("0"), align="center", font=("Courier", 12, "normal"))
    _window.mainloop()


def update_window():
    _window.update()


def play_intro_song():
    update_window()
    winsound.PlaySound("music/Pacman_intro.wav", winsound.SND_ASYNC)
    time.sleep(4)


def game_over():
    if not get_player().alive:
        return True
    return False


# Window properties
_window = turtle.Screen()
