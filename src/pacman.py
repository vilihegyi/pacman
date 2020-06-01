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

# Main game loop
while not game_over():
    elapsed_time = time.time()
    update_window()
    move_player()
    check_collision(red_ghost)
    if ghosts_released:
        move_orange_ghost()
        move_red_ghost()
        move_pink_ghost()
        move_turquoise_ghost()
    if elapsed_time - start_time > 10 and not ghosts_released:
        release_ghosts()
        ghosts_released = True

# Don't close the window one the game is over
minutes, seconds = divmod(elapsed_time - start_time, 60)
print("Game finished in: %d:%d" % (minutes, seconds))
end_game()
