import pygame
import consts
import game_field
import screen
import soldier

state = {
    "state": consts.WELCOME_STATE,
    "player_status": consts.SOLDIER_MOVE,
    "is_window_open": True,
}


def check_soldier_status():
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
                soldier.right(field)
                check_soldier_status()
            if event.key == pygame.K_LEFT:
                soldier.left(field)
                check_soldier_status()
            if event.key == pygame.K_UP:
                soldier.up(field)
                check_soldier_status()
            if event.key == pygame.K_DOWN:
                soldier.down(field)
                check_soldier_status()
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
        screen.draw_game(state)


if __name__ == '__main__':
    main()
