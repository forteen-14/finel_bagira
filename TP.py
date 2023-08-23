import consts
import random
import pygame
import soldier


def check_if_can_teleport(field, random_tp):
    soldier_position = soldier.get_soldier_position(field)
    for i in soldier_position:
        #check if the soldier is not in a mine or flag
        if field[i[0]][i[1]] == consts.MINE or field[i[0]][i[1]+1] == consts.MINE or field[i[0]+1][i[1]] == consts.MINE or\
                field[i[0]+1][i[1]+1] == consts.MINE or field[i[0]+2][i[1]] == consts.MINE or field[i[0]+2][i[1]+1] == consts.MINE or \
                field[i[0]+3][i[1]] == consts.MINE or field[i[0]+3][i[1]+1]:
            return True
        else:
            return False


def teleport_the_player(field, tp_list):
    while True:
        is_good_place = random_tp = random.choice(tp_list)
        if is_good_place:
            break
    #delete the soldier from the field
    for i in soldier.get_soldier_position(field):
        field[i[0]][i[1]] = consts.EMPTY

    #put the soldier in the new place
    for i in range(consts.SOLDIER_HIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            field[random_tp[0]+i][random_tp[1]+j] = consts.SOLDIER


