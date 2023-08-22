import consts
import pygame

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_grid():
      # Set the size of the grid block
    for x in range(0, consts.WINDOW_WIDTH, consts.BLOCK_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.BLOCK_SIZE):
            rect = pygame.Rect(x, y, consts.BLOCK_SIZE, consts.BLOCK_SIZE)
            pygame.draw.rect(screen, consts.BLACK, rect, 1)

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
def draw_welcome():
    draw_message(consts.WELCOME_MESSAGE,consts.WELCOME_FONT_SIZE,consts.WELCOME_COLOR,consts.WELCOME_LOCATION)
def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_grid()
    if state["state"]==consts.WELCOME_STATE:
        draw_welcome()
    pygame.display.flip()