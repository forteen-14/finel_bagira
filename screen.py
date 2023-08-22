import consts
import pygame

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

objects={"soldier":[pygame.image.load(consts.SOLIDER_PNG_PATH),consts.SOLDIER_SIZE,consts.SOLDIER],
         "bush":[pygame.image.load(consts.BUSH_PNG_PATH),consts.BUSH_SIZE,consts.GRASS],
         "mine":[pygame.image.load(consts.MINE_PNG_PATH),consts.MINE_SIZE,consts.MINE],
         "flag":[pygame.image.load(consts.FLAG_PNG_PATH),consts.FLAG_SIZE,consts.FLAG]
         }
object_pixales={"soldier": 8,
               "bush": 1,
               "mine": 3,
               "flag": 12}
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
    draw_message(consts.WELCOME_MESSAGE, consts.WELCOME_FONT_SIZE, consts.WELCOME_COLOR, consts.WELCOME_LOCATION)




def draw_image(name,obj_info,field):
    loaded_img=obj_info[0]
    size=obj_info[1]
    object_index=obj_info[2]
    img=loaded_img
    img = pygame.transform.scale(img,size)
    count_pixales=0
    for row in range(consts.BOARD_GRID_COLS):
        for col in range(consts.BOARD_GRID_ROW):
            if field[col][row]==object_index:

                if count_pixales==0:
                    screen.blit(img, (row * consts.BLOCK_SIZE, col * consts.BLOCK_SIZE))
                    count_pixales=object_pixales[name]


                count_pixales-=1





def draw_game(state,field):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_grid()
    if state["state"] == consts.WELCOME_STATE:
        draw_welcome()

    for name,info in objects.items():
        draw_image(name,info,field)
    

    pygame.display.flip()
