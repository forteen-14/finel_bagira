import consts
import random
import pygame
import soldier


def check_if_can_teleport(field, random_tp):
    soldier_position = soldier.get_soldier_position(field)
    for i in soldier_position:
        #check if the soldier is not in a mine or flag
        if field[i[0]][i[1]] == consts.MINE or field[i[0]][i[1]] == consts.FLAG:
            return True


def teleport_the_player(field, tp_list):
    soldier_position = soldier.get_soldier_position(field)
    random_tp = random.choice(tp_list)
