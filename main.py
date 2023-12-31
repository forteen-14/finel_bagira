import pygame
import consts
import game_field
import screen
import soldier
import time
import DataBase
import copy
import TP
import guard

state = {
    "state": consts.WELCOME_STATE,
    "player_status": consts.SOLDIER_MOVE,
    "is_window_open": True,
    "is_key_load": consts.NEUTRAL_STATE,
    "what_number_pressed": consts.DEFAULT_KEY_LOAD_AND_SAVE,
    "guard_Direction": consts.GUARD_RIGHT,
    "object_hitted": consts.EMPTY
}






# parameters: field, start_count, tp_list,field_copy
# return: start_count
# this function handle the events according to the state
def event_handler(field, start_count, tp_list,field_copy):
    # Cycles through all the events currently occuring
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.move(field,consts.RIGHT,field_copy)
                soldier.check_soldier_status(state, field, tp_list)
            if event.key == pygame.K_LEFT and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.move(field,consts.LEFT,field_copy)
                soldier.check_soldier_status(state, field, tp_list)
            if event.key == pygame.K_UP and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.move(field,consts.UP,field_copy)
                soldier.check_soldier_status(state, field, tp_list)
            if event.key == pygame.K_DOWN and event.type == pygame.KEYDOWN:
                state["player_status"] = soldier.move(field,consts.DOWN,field_copy)
                soldier.check_soldier_status(state, field, tp_list)
            if event.key == pygame.K_ESCAPE and event.type == pygame.KEYDOWN:
                state["is_window_open"] = False
            if event.key == pygame.K_SPACE:
                state["state"] = consts.SPACE_X_RAY
            if (
                event.unicode.isdigit() and event.type == pygame.KEYDOWN
            ):  # if the key is a number

                start_count = pygame.time.get_ticks()
                return start_count
            if event.type == pygame.KEYUP:
                if event.unicode.isdigit():
                    space_end = pygame.time.get_ticks()
                    if space_end - start_count >= consts.SAVE_PRESS_TIME:
                        state["is_key_load"] = consts.SAVE_STATE
                        state["what_number_pressed"] = event.unicode

                    else:
                        state["is_key_load"] = consts.LOAD_STATE
                        state["what_number_pressed"] = event.unicode


            elif state["state"] != consts.RUNNING_STATE:
                continue
    return start_count



# parameters: None
# return: None
# this function reset the load and save state
def rest_load_and_save():
    state["is_key_load"] = consts.NEUTRAL_STATE
    state["what_number_pressed"] = consts.DEFAULT_KEY_LOAD_AND_SAVE
    time.sleep(consts.LOAD_GAME_MSG_TIME)


# parameters: field_copy
# return: None
# this function fix the copy field
def fix_copy_field(field_copy):
    # make the copy field empty where a soldier and a guard are
    for i in range(consts.SOLDIER_HIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            field_copy[i][j] = consts.EMPTY
    for i in range(consts.GUARD_HIGHT):
        for j in range(consts.GUARD_WIDTH):
            field_copy[i + consts.GUARD_START_POINT[0]][j + consts.GUARD_START_POINT[1]] = consts.EMPTY


def main():
    tp_list = []
    is_third_loop = 0
    DataBase.DataBase()
    start_count = 0
    pygame.init()
    field = game_field.create_field(tp_list)
    field_copy = copy.deepcopy(field)
    fix_copy_field(field_copy)
    while state["is_window_open"]:
        start_count = event_handler(field, start_count, tp_list,field_copy)

        if state["state"] == consts.RUNNING_STATE:
            if is_third_loop == consts.GUARD_SLOW_SPEED:
                guard.update_guard_status(state, field, state["guard_Direction"])
                is_third_loop = 0
            else:
                is_third_loop += 1


            game_field.fix_field(field, field_copy)
            soldier.check_if_suldier_guard_hit(field,state)


        screen.draw_game(state, field, field_copy)
        # load and save ==================
        if state["is_key_load"] == consts.LOAD_STATE:
            f, f_c = DataBase.loadGame(state["what_number_pressed"])
            if f!=None and f_c!=None:
                field, field_copy=f,f_c
            rest_load_and_save()
        elif state["is_key_load"] == consts.SAVE_STATE:
            DataBase.SaveGame(state["what_number_pressed"], field, field_copy)
            rest_load_and_save()
        # =============================

        if state["state"] == consts.SPACE_X_RAY:
            state["state"] = consts.RUNNING_STATE
            time.sleep(consts.X_RAY_TIME)
        if state["state"] == consts.WIN_STATE or state["state"] == consts.LOSE_STATE:
            time.sleep(consts.TIME_DELAY)
            exit(0)


if __name__ == "__main__":
    main()
