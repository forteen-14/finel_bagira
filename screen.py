import consts
import pygame
import time
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




def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_welcome():
    draw_message(consts.WELCOME_MESSAGE, consts.WELCOME_FONT_SIZE, consts.WELCOME_COLOR, consts.WELCOME_LOCATION)




def draw_image(name,obj_info,field):
    loaded_img,size,object_index=obj_info
    img=loaded_img
    img = pygame.transform.scale(img,size)
    count_pixales=0
    for row in range(consts.BOARD_GRID_ROW):
        for col in range(consts.BOARD_GRID_COLS):
            if field[row][col]==object_index:
                if count_pixales==0:
                    screen.blit(img, (col * consts.BLOCK_SIZE, row * consts.BLOCK_SIZE))
                    count_pixales=object_pixales[name]
                count_pixales-=1


def dead(field):
    photos=[pygame.image.load(consts.BANG_PATH),pygame.image.load(consts.SOLDIER_DEATH_PATH)]
    for i in range(len(photos)):
        draw_image("soldier",[photos[i],consts.SOLDIER_SIZE,consts.SOLDIER],field)
def draw_lose_message():

    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)




def x_ray():
    # Set the size of the grid block
    screen.fill(consts.BLACK)
    for x in range(0, consts.WINDOW_WIDTH, consts.BLOCK_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.BLOCK_SIZE):
            rect = pygame.Rect(x, y, consts.BLOCK_SIZE, consts.BLOCK_SIZE)
            pygame.draw.rect(screen, consts.GRAY, rect, 1)

def draw_game(state,field):
    screen.fill(consts.BACKGROUND_COLOR)
    def x_ray_handle():
        x_ray()
        time.sleep(consts.X_RAY_TIME)
        draw_image(consts.SHOW_ON_XRAY, objects[consts.SHOW_ON_XRAY], field)

    if state["state"] == consts.WELCOME_STATE:
        draw_welcome()
    elif state["state"] == consts.SPACE_X_RAY:
        x_ray_handle()
        state["state"] = consts.RUNNING_STATE
    for name,info in objects.items():
        if name!="mine":
            draw_image(name,info,field)
    if state["state"]==consts.LOSE_STATE:
        x_ray_handle()
        dead(field)
        draw_lose_message()
    elif state["state"]==consts.WIN_STATE:
        draw_win_message()


    pygame.display.flip()
