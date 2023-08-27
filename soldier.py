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


# parameters: field
# return: the status of the soldier
# this function return the status of the soldier after he moved and makes the move one step to the right
def right(field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        next_position_info = field[i[0]][i[1]+1]
        if 0 <= i[0] < consts.BOARD_GRID_ROW and 0 <= i[1] +1 < consts.BOARD_GRID_COLS:
            if count >= 6:
                if next_position_info == consts.MINE:
                    return consts.SOLDIER_MINE_HIT
                if next_position_info == consts.TELEPORT:
                    return consts.SOLDIER_TELEPORT
            if count < 6:
                if next_position_info == consts.FLAG:
                    return consts.SOLDIER_FLAG_HIT
            if next_position_info == consts.GUARD:
                return consts.SOLDIER_GUARD_HIT
        else:
            return "out of bounds"
        count += 1

    for i in range(0, len(soldier_position), 2):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]][soldier_position[i][1] + 2] = consts.SOLDIER
    return "move"


# parameters: field
# return: the status of the soldier
# this function return the status of the soldier after he moved and makes the move one step to the left
def left(field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        next_position_info = field[i[0]][i[1]-1]
        if 0 <= i[0] < consts.BOARD_GRID_ROW and 0 <= i[1] - 1 < consts.BOARD_GRID_COLS:
            if count >= 6:
                if next_position_info == consts.MINE:
                    return consts.SOLDIER_MINE_HIT
                if next_position_info == consts.TELEPORT:
                    return consts.SOLDIER_TELEPORT
            if count < 6:
                if next_position_info == consts.FLAG:
                    return consts.SOLDIER_FLAG_HIT
            if next_position_info == consts.GUARD:
                return consts.SOLDIER_GUARD_HIT
        else:
            return "out of bounds"
        count += 1

    for i in range(1, len(soldier_position), 2):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]][soldier_position[i][1] - 2] = consts.SOLDIER
    return "move"


# parameters: field
# return: the status of the soldier
# this function return the status of the soldier after he moved and makes the move one step down
def down(field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        next_position_info = field[i[0]+1][i[1]]
        if 0 <= i[0]+1 < consts.BOARD_GRID_ROW and 0 <= i[1] < consts.BOARD_GRID_COLS:
            if count >= 6:
                if next_position_info == consts.MINE:
                    return consts.SOLDIER_MINE_HIT
                if next_position_info == consts.TELEPORT:
                    return consts.SOLDIER_TELEPORT
            if count < 6:
                if next_position_info == consts.FLAG:
                    return consts.SOLDIER_FLAG_HIT
            if next_position_info == consts.GUARD:
                return consts.SOLDIER_GUARD_HIT
        else:
            return "out of bounds"
        count += 1

# go in reverse order to not change the position of the soldier
    for i in range(len(soldier_position)-1, -1, -1):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]+1][soldier_position[i][1]] = consts.SOLDIER
    return "move"


# parameters: field
# return: the status of the soldier
# this function return the status of the soldier after he moved and makes the move one step up
def up(field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        next_position_info = field[i[0]+1][i[1]]
        if 0 <= i[0]-1 < consts.BOARD_GRID_ROW and 0 <= i[1] < consts.BOARD_GRID_COLS:
            if count >= 6:
                if next_position_info == consts.MINE:
                    return consts.SOLDIER_MINE_HIT
                if next_position_info == consts.TELEPORT:
                    return consts.SOLDIER_TELEPORT
            if count < 6:
                if next_position_info == consts.FLAG:
                    return consts.SOLDIER_FLAG_HIT
            if next_position_info == consts.GUARD:
                return consts.SOLDIER_GUARD_HIT
        else:
            return "out of bounds"
        count += 1

    for i in range(len(soldier_position)):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]-1][soldier_position[i][1]] = consts.SOLDIER
    return "move"


# parameters: state, field, tp_list
# return: None
# this function checks the status of the soldier and change the state accordingly
def check_soldier_status(state,field,tp_list):
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
