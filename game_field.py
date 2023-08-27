import consts
import random

mobs=[consts.SOLDIER,consts.GUARD]
def fix_field(field, field_copy):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] in mobs:
                continue
            else:
                field[row][col] = field_copy[row][col]
            if field[row][col]==consts.SOLDIER:
                field[row][col]=consts.EMPTY


def create_characters(field):
    # make the soldier take 2X4 spots in the top left and the flag 3X4 in the bottom right
    for row in range(4):
        for col in range(2):
            field[row][col] = consts.SOLDIER
    for row in range(4):
        for col in range(3):
            field[consts.BOARD_GRID_ROW - row - 1][consts.BOARD_GRID_COLS - col - 1] = consts.FLAG


def create_grass(field):
    for i in range(consts.GRASS_AMOUNT):
        # check if the spot is already taken ny soldier or flag
        while True:
            row = random.randint(0, consts.BOARD_GRID_ROW - 1)
            col = random.randint(0, consts.BOARD_GRID_COLS - 1)
            if field[row][col] == consts.EMPTY:
                field[row][col] = consts.GRASS
                break


def create_mines(field):
    # put 20 random mines
    for i in range(consts.MINES_AMOUNT):
        # check if the spot is already taken ny soldier or flag
        while True:
            # mines take 3 spots in a row
            row = random.randint(0, consts.BOARD_GRID_ROW - 1)
            col = random.randint(0, consts.BOARD_GRID_COLS - 3)
            if field[row][col] == consts.EMPTY and field[row][col + 1] == consts.EMPTY and field[row][
                col + 2] == consts.EMPTY:
                field[row][col] = consts.MINE
                field[row][col + 1] = consts.MINE
                field[row][col + 2] = consts.MINE
                break


def create_teleports(field, tp_list):
    # put 5 random teleports
    for i in range(consts.TELEPORT_AMOUNT):
        # teleports take 3 spots in a row and it can only be between 4-20 rows
        while True:
            row = random.randint(4, consts.BOARD_GRID_ROW - 4)
            col = random.randint(4, consts.BOARD_GRID_COLS - 20)
            if field[row][col] == consts.EMPTY and field[row][col + 1] == consts.EMPTY and field[row][
                col + 2] == consts.EMPTY:
                field[row][col] = consts.TELEPORT
                field[row][col + 1] = consts.TELEPORT
                field[row][col + 2] = consts.TELEPORT
                tp_list.append([row, col + 1])
                break


def create_guard(field):
    # put the guard in the GUARD_START_POINT
    for row in range(consts.GUARD_HIGHT):
        for col in range(consts.GUARD_WIDTH):
            field[consts.GUARD_START_POINT[0] + row][consts.GUARD_START_POINT[1] + col] = consts.GUARD


def print_field(field):
    for row in field:
        print(row)


def create_field(tp_list):
    # create the field 2d list
    game_filed = [[consts.EMPTY for col in range(consts.BOARD_GRID_COLS)] for row in range(consts.BOARD_GRID_ROW)]
    create_characters(game_filed)
    create_guard(game_filed)
    create_mines(game_filed)
    create_teleports(game_filed, tp_list)
    create_grass(game_filed)
    return game_filed
