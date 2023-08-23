import consts
import random
import pygame
import soldier


def check_if_can_teleport(field, tp_list):



def teleport_the_player(field, tp_list):
    soldier_position = soldier.get_soldier_position(field)
    random_tp = random.choice(tp_list)
