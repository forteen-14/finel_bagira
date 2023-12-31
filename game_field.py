import consts
import random

mobs = [consts.SOLDIER, consts.GUARD]

# parameters: field and field_copy
# return: None
# this function fix the field after the soldier moved
def fix_field(field, field_copy):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if not field[row][col] == consts.SOLDIER and not field[row][col] == consts.GUARD:
                field[row][col] = field_copy[row][col]
            elif field[row][col] == consts.SOLDIER and field_copy[row][col] == consts.FLAG and field[row][col] == consts.GUARD:
                field[row][col] = field_copy[row]



def create_soldier(field):
    # make the soldier take 2X4 spots in the top left and the flag 3X4 in the bottom right
    for row in range(4):
        for col in range(2):
            field[row][col] = consts.SOLDIER
def create_flag(field):
    for row in range(4):
        for col in range(3):
            field[consts.BOARD_GRID_ROW - row - 1][
                consts.BOARD_GRID_COLS - col - 1
                ] = consts.FLAG




# parameters: field
# return: None
# this function create the grass in the field
def create_grass(field):
    for i in range(consts.GRASS_AMOUNT):
        # check if the spot is already taken ny soldier or flag
        while True:
            row = random.randint(0, consts.BOARD_GRID_ROW - 1)
            col = random.randint(0, consts.BOARD_GRID_COLS - 1)
            if field[row][col] == consts.EMPTY:
                field[row][col] = consts.GRASS
                break


# parameters: field
# return: None
# this function create the mines in the field
def create_mines(field):
    # put 20 random mines
    for i in range(consts.MINES_AMOUNT):
        # check if the spot is already taken ny soldier or flag
        while True:
            # mines take 3 spots in a row
            row = random.randint(0, consts.BOARD_GRID_ROW - 1)
            col = random.randint(0, consts.BOARD_GRID_COLS - 3)
            if (
                field[row][col] == consts.EMPTY
                and field[row][col + 1] == consts.EMPTY
                and field[row][col + 2] == consts.EMPTY
            ):
                field[row][col] = consts.MINE
                field[row][col + 1] = consts.MINE
                field[row][col + 2] = consts.MINE
                break


# parameters: field and tp_list
# return: None
# this function create the teleports in the field
def create_teleports(field, tp_list):
    # put 5 random teleports
    for i in range(consts.TELEPORT_AMOUNT):
        # teleports take 3 spots in a row and it can only be between 4-20 rows
        while True:
            row = random.randint(4, consts.BOARD_GRID_ROW - 4)
            col = random.randint(4, consts.BOARD_GRID_COLS - 20)
            if (
                field[row][col] == consts.EMPTY
                and field[row][col + 1] == consts.EMPTY
                and field[row][col + 2] == consts.EMPTY
            ):
                field[row][col] = consts.TELEPORT
                field[row][col + 1] = consts.TELEPORT
                field[row][col + 2] = consts.TELEPORT
                tp_list.append([row, col + 1])
                break


# parameters: field
# return: None
# this function create the guard in the field
def create_guard(field):
    # put the guard in the GUARD_START_POINT
    for row in range(consts.GUARD_HIGHT):
        for col in range(consts.GUARD_WIDTH):
            field[consts.GUARD_START_POINT[0] + row][
                consts.GUARD_START_POINT[1] + col
            ] = consts.GUARD


# parameters: field
# return: None
# this function print the field
def print_field(field):
    for row in field:
        print(row)


# parameters: tp_list
# return: None
# this function crate the tp_list
def create_field(tp_list):
    # create the field 2d list
    game_filed = [
        [consts.EMPTY for col in range(consts.BOARD_GRID_COLS)]
        for row in range(consts.BOARD_GRID_ROW)
    ]
    create_soldier(game_filed)
    create_flag(game_filed)
    create_guard(game_filed)
    create_mines(game_filed)
    create_teleports(game_filed, tp_list)
    create_grass(game_filed)
    return game_filed
