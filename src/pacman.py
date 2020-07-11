# Personal libraries
from window import *
from ghost import *

init_game()
place_fruits()
player = create_player()
player.has_moved = False
create_ghosts()
ghosts_released = False

play_intro_song()
start_time = time.time()
elapsed_time = time.time()
after_time = start_time

# Main game loop
while not game_over():
    elapsed_time = time.time()
    update_window()
    move_player()
    if elapsed_time - start_time > 4 and not ghosts_released:
        release_ghosts()
        ghosts_released = True

    if red_ghost.distance(get_player()) < 100:
        time_interval = 1
    else:
        time_interval = 0.5
    check_collision(orange_ghost)
    check_collision(red_ghost)
    check_collision(pink_ghost)
    check_collision(turquoise_ghost)
    if ghosts_released and (elapsed_time - after_time > time_interval):
        after_time = elapsed_time
        move_ghost(orange_ghost)
        move_ghost(red_ghost)
        move_ghost(pink_ghost)
        move_ghost(turquoise_ghost)

# Don't close the window one the game is over
minutes, seconds = divmod(elapsed_time - start_time, 60)
print("Game finished in: %d:%d" % (minutes, seconds))
end_game()
