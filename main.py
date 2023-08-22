import pygame
import consts
import game_field
import screen
import soldier
import time

state = {
    "state": consts.WELCOME_STATE,
    "player_status": consts.SOLDIER_MOVE,
    "is_window_open": True,

}


def check_soldier_status(field):
    if state["player_status"] == consts.SOLDIER_MINE_HIT:
        state["state"] = consts.LOSE_STATE

    elif state["player_status"] == consts.SOLDIER_FLAG_HIT:
        state["state"] = consts.WIN_STATE
    elif state["player_status"] == consts.SOLDIER_OUT_OF_BOUNDS:
        state["state"] = consts.RUNNING_STATE
    elif state["player_status"] == consts.SOLDIER_MOVE:
        state["state"] = consts.RUNNING_STATE


def event_handler(field):
    # Cycles through all the events currently occuring
    for event in pygame.event.get():
        # Condition becomes true when keyboard is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                state["player_status"] = soldier.right(field)
                check_soldier_status(field)
            if event.key == pygame.K_LEFT:
                state["player_status"] = soldier.left(field)
                check_soldier_status(field)
            if event.key == pygame.K_UP:
                state["player_status"] = soldier.up(field)
                check_soldier_status(field)
            if event.key == pygame.K_DOWN:
                state["player_status"] = soldier.down(field)
                check_soldier_status(field)
            if event.key == pygame.K_ESCAPE:
                state["is_window_open"] = False
            elif state["state"] != consts.RUNNING_STATE:
                continue


def main():
    pygame.init()
    field = game_field.create_field()
    game_field.print_field(field)
    while state["is_window_open"]:
        event_handler(field)
        screen.draw_game(state,field)
        if state["state"]==consts.WIN_STATE or state["state"]==consts.LOSE_STATE:
            time.sleep(3)
            exit(0)


if __name__ == '__main__':
    main()
