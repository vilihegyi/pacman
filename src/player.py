import turtle


# Player
def create_player():
    _player.speed(0)
    _player.shape("pictures/Pacman_right.gif")
    _player.color("yellow")
    _player.penup()
    _player.goto(0, -40)  # Make sure character is in center of the screen
    _player.direction = ""
    _player.alive = True
    _player.score = 0
    return _player


def get_player():
    return _player


def update_score(score):
    _pen.clear()
    _pen.write("Score:\n{}".format(score), align="center", font=("Courier", 12, "normal"))


_player = turtle.Turtle()
# Display score
_pen = turtle.Turtle()
_pen.hideturtle()
_pen.speed(0)
_pen.shape("square")
_pen.color("white")
_pen.penup()
_pen.goto(-220, 0)
_pen.write("Score:\n{}".format("0"), align="center", font=("Courier", 12, "normal"))
