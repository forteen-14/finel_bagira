import consts
import game_field


def get_soldier_position(field):
    found_soldier = []
    tmp_list = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == consts.SOLDIER:
                tmp_list = [row, col]
                found_soldier.append(tmp_list)
    return found_soldier


def right(field, show_field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        if 0 <= i[0] < consts.BOARD_GRID_ROW and 0 <= i[1] +1 < consts.BOARD_GRID_COLS:
            if field[i[0]][i[1]+1] == consts.MINE:
                if count >= 6:
                    return "hit mine"
                else:
                    pass
                if field[i[0]][i[1]+1] == consts.FLAG:
                    if count < 6:
                        return "win"
                    else:
                        left(field, show_field)
        else:
            return "out of bounds"
        count += 1

    for i in range(0, len(soldier_position), 2):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]][soldier_position[i][1] + 2] = consts.SOLDIER
    return "move"


def left(field, show_field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        if 0 <= i[0] < consts.BOARD_GRID_ROW and 0 <= i[1] -1 < consts.BOARD_GRID_COLS:
            if count >= 6:
                if field[i[0]-1][i[1]] == consts.MINE:
                    return "hit mine"
            if field[i[0]-1][i[1]] == consts.FLAG:
                if count < 6:
                    return "win"
                else:
                    right(field, show_field)
        else:
            return "out of bounds"
        count += 1

    for i in range(1, len(soldier_position), 2):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]][soldier_position[i][1] - 2] = consts.SOLDIER
    return "move"


def down(field, show_field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        if 0 <= i[0]+1 < consts.BOARD_GRID_ROW and 0 <= i[1] < consts.BOARD_GRID_COLS :
            if count >= 6:
                if field[i[0]+1][i[1]] == consts.MINE:
                    return "hit mine"
                if field[i[0]+1][i[1]] == consts.FLAG:
                    if count < 6:
                        return "win"
                    else:
                        up(field, show_field)
        else:
            return "out of bounds"
        count += 1

# go in reverse order to not change the position of the soldier
    for i in range(len(soldier_position)-1, -1, -1):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]+1][soldier_position[i][1]] = consts.SOLDIER
    return "move"


def up(field, show_field):
    count = 0
    soldier_position = get_soldier_position(field)
    for i in soldier_position:
        if 0 <= i[0]-1 < consts.BOARD_GRID_ROW and 0 <= i[1] < consts.BOARD_GRID_COLS:
            if count >= 6:
                if field[i[0]-1][i[1]] == consts.MINE:
                    return "hit mine"
            if field[i[0]-1][i[1]] == consts.FLAG:
                if count < 6:
                    return "win"
                else:
                    down(field, show_field)
        else:
            return "out of bounds"
        count += 1

    for i in range(len(soldier_position)):
        field[soldier_position[i][0]][soldier_position[i][1]] = consts.EMPTY
        field[soldier_position[i][0]-1][soldier_position[i][1]] = consts.SOLDIER
    return "move"

