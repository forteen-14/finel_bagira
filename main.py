import pygame
import consts
import game_field
import screen
import soldier

state = {
    "State": consts.RUNNING_STATE,
    "is_window_open": True,
}



def event_handler():
    while state["is_window_open"]:
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


def main():
    # initialize pygame screen
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption(consts.GAME_NAME)
    screen.fill(consts.DARK_GREEN)
    pygame.display.flip()
    field = game_field.create_field()
    event_handler()
    state["is_window_open"]


if __name__ == '__main__':
    main()











