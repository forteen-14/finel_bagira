import consts
import game_field
import TP


# parameters: field
# return: list of the soldier position
# this function return the position of the soldier in the field
def get_soldier_position(field):
    found_soldier = []
    tmp_list = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == consts.SOLDIER:
                tmp_list = [row, col]
                found_soldier.append(tmp_list)
    return found_soldier




def chose_direction(direct):
    if direct==consts.LEFT:
        return (0,-1)
    elif direct==consts.RIGHT:
        return (0,1)
    elif direct==consts.DOWN:
        return (1,0)
    elif direct==consts.UP:
        return (-1,0)


def actual_move(field,soldier_position,pos):
    new_pos = []
    for i in range(len(soldier_position)):
        new_pos.append([soldier_position[i][0] + pos[0], soldier_position[i][1] + pos[1]])

    for i in range(len(soldier_position)):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
    for i in range(len(soldier_position)):
        field[new_pos[i][0]][new_pos[i][1]] = consts.SOLDIER


def move(field,direction,field_copy):
    pos=chose_direction(direction)
    count = 0
    soldier_position = get_soldier_position(field)
    stat=""
    for i in soldier_position:
        next_position_info = field_copy[i[0] + pos[0]][i[1]+pos[1]]
        if 0 <= i[0] + pos[0] < consts.BOARD_GRID_ROW and 0 <= i[1]+pos[1] < consts.BOARD_GRID_COLS:
            if count >= 6:
                if next_position_info == consts.MINE:
                    stat = consts.SOLDIER_MINE_HIT
                    break
                if next_position_info == consts.TELEPORT:
                    stat = consts.SOLDIER_TELEPORT
                    break

            if next_position_info == consts.FLAG:
                stat = consts.SOLDIER_FLAG_HIT
                break
            if next_position_info == consts.GUARD:
                stat = consts.SOLDIER_GUARD_HIT
                break
        else:
            return consts.SOLDIER_OUT_OF_BOUNDS
        count += 1

    # go in reverse order to not change the position of the soldier

    actual_move(field,soldier_position,pos)
    if stat=="":
        stat = consts.SOLDIER_MOVE
    return stat


# parameters: state, field, tp_list
# return: None
# this function checks the status of the soldier and change the state accordingly
def check_soldier_status(state, field, tp_list):
    if state["player_status"] == consts.SOLDIER_MINE_HIT:
        state["state"] = consts.LOSE_STATE
    elif state["player_status"] == consts.SOLDIER_TELEPORT:
        TP.teleport_the_player(field, tp_list)
        state["state"] = consts.RUNNING_STATE
    elif state["player_status"] == consts.SOLDIER_FLAG_HIT:
        state["state"] = consts.WIN_STATE
    elif state["player_status"] == consts.SOLDIER_OUT_OF_BOUNDS:
        state["state"] = consts.RUNNING_STATE
    elif state["player_status"] == consts.SOLDIER_MOVE:
        state["state"] = consts.RUNNING_STATE
    elif state["player_status"] == consts.SOLDIER_GUARD_HIT:
        state["state"] = consts.LOSE_STATE


def check_if_suldier_guard_hit(field,state):
    if len(get_soldier_position(field)) < consts.SOLDIER_PIXALES:
        state["state"] = consts.LOSE_STATE
        state["object_hitted"]=consts.GUARD