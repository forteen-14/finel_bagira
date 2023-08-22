import pygame
import consts
import game_field
import screen
import soldier

state = {
    "state": consts.WELCOME_STATE,
    "is_window_open": True,
}




def event_handler():
        # Cycles through all the events currently occuring
        for event in pygame.event.get():

            # Condition becomes true when keyboard is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_ESCAPE:
                    state["is_window_open"] = False
                elif state["state"] != consts.RUNNING_STATE:
                    continue


def print_field(field):
    for row in field:
        print(row)


def main():
    pygame.init()
    field = game_field.create_field()
    print_field(field)
    while state["is_window_open"]:
        event_handler()
        screen.draw_game(state)


if __name__ == '__main__':
    main()










