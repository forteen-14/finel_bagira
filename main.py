import pygame
import consts
import game_field
import screen
import soldier
import time
import DataBase
import copy

state = {
    "state": consts.WELCOME_STATE,
    "player_status": consts.SOLDIER_MOVE,
    "is_window_open": True,
    "is_key_load": consts.NEUTRAL_STATE,
    "what_number_pressed": consts.DEFAULT_KEY_LOAD_AND_SAVE


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


def event_handler(field, start_count):
    # Cycles through all the events currently occuring
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.right(field)
                check_soldier_status(field)
            if event.key == pygame.K_LEFT and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.left(field)
                check_soldier_status(field)
            if event.key == pygame.K_UP and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.up(field)
                check_soldier_status(field)
            if event.key == pygame.K_DOWN and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.down(field)
                check_soldier_status(field)
            if event.key == pygame.K_ESCAPE and event.type == pygame.KEYDOWN:
                state["is_window_open"] = False
            if event.key == pygame.K_SPACE:
                state["state"] = consts.SPACE_X_RAY
            if event.unicode.isdigit() and event.type == pygame.KEYDOWN : # if the key is a number
                print("number pressed")
                start_count = pygame.time.get_ticks()
                return start_count
            if event.type == pygame.KEYUP:
                if event.unicode.isdigit():
                    space_end = pygame.time.get_ticks()
                    if space_end - start_count >= 1000:
                        state["is_key_load"] = consts.SAVE_STATE
                        state["what_number_pressed"] = event.unicode
                        print("save")
                    else:
                        state["is_key_load"] = consts.LOAD_STATE
                        state["what_number_pressed"] = event.unicode
                        print("load")

            elif state["state"] != consts.RUNNING_STATE:
                continue
    return start_count


def fix_field(field, field_copy):
    for row in range(2, len(field)):
        for col in range(4, len(field[row])):
            if not field[row][col] == consts.SOLDIER:
                field[row][col] = field_copy[row][col]
            if field[row][col] == consts.SOLDIER and field_copy[row][col] == consts.FLAG:
                field[row][col] = field_copy[row][col]


def main():
    DataBase.DataBase()
    start_count = 0
    pygame.init()
    field = game_field.create_field()
    field_copy = game_field.create_field()
    game_field.print_field(field)
    while state["is_window_open"]:
        start_count = event_handler(field, start_count)
        if state["state"] == consts.RUNNING_STATE:
            fix_field(field, field_copy)
        screen.draw_game(state, field)
        if state["is_key_load"] == consts.LOAD_STATE:
            print("load")
            DataBase.loadGame(state["what_number_pressed"])
        elif state["is_key_load"] == consts.SAVE_STATE:
            DataBase.SaveGame(state["what_number_pressed"], field)
            print("save")
        if state["state"]==consts.WIN_STATE or state["state"]==consts.LOSE_STATE:
            time.sleep(consts.TIME_DELAY)
            exit(0)



if __name__ == '__main__':
    main()
