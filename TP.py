import consts
import random
import pygame
import soldier


def teleport_the_player(field, tp_list):
    soldier_position = soldier.get_soldier_position(field)
    #get random teleport from the list
    random_tp = random.choice(tp_list)


    return "move"