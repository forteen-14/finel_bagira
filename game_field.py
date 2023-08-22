import consts
import random


def create_characters(field):

    #make the soldier take 2X4 spots in the top left and the flag 3X4 in the bottom right
    for row in range(4):
        for col in range(2):
            field[row][col] = consts.SOLDIER
    for row in range(4):
        for col in range(3):
            field[consts.BOARD_GRID_ROW - row - 1][consts.BOARD_GRID_COLS - col - 1] = consts.FLAG
    #put 20 random grass spots
    for i in range(consts.GRASS_AMOUNT):
        #check if the spot is already taken ny soldier or flag
        while True:
            row = random.randint(0, consts.BOARD_GRID_ROW - 1)
            col = random.randint(0, consts.BOARD_GRID_COLS - 1)
            if field[row][col] != consts.SOLDIER and field[row][col] != consts.FLAG:
                field[row][col] = consts.GRASS
                break


def create_mines(field):
    #put 20 random mines
    for i in range(consts.MINES_AMOUNT):
        try:
        #check if the spot is already taken ny soldier or flag
            while True:
                #mines take 3 spots in a row
                row = random.randint(0, consts.BOARD_GRID_ROW - 1)
                col = random.randint(0, consts.BOARD_GRID_COLS - 3)
                if field[row][col] != consts.SOLDIER and field[row][col] != consts.FLAG and field[row][col + 1] != consts.SOLDIER and field[row][col + 1] != consts.FLAG and field[row][col + 2] != consts.SOLDIER and field[row][col + 2] != consts.FLAG:
                    field[row][col] = consts.MINE
                    field[row][col + 1] = consts.MINE
                    field[row][col + 2] = consts.MINE
                    break
        except:
            pass


def create_field():
    # create the field 2d list
    game_filed = [[consts.EMPTY for col in range(consts.BOARD_GRID_COLS)] for row in range(consts.BOARD_GRID_ROW)]
    create_characters(game_filed)
    create_mines(game_filed)


    return game_filed



















