import consts
import pygame
import time

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

objects = {
    "bush": [
        pygame.image.load(consts.BUSH_PNG_PATH),
        consts.BUSH_SIZE,
        consts.GRASS,
        consts.BUSH_PIXALES,
    ],
    "mine": [
        pygame.image.load(consts.MINE_PNG_PATH),
        consts.MINE_SIZE,
        consts.MINE,
        consts.MINE_PIXALES,
    ],
    "flag": [
        pygame.image.load(consts.FLAG_PNG_PATH),
        consts.FLAG_SIZE,
        consts.FLAG,
        consts.FLAG_PIXALES,
    ],
    "soldier": [
        pygame.image.load(consts.SOLIDER_PNG_PATH),
        consts.SOLDIER_SIZE,
        consts.SOLDIER,
        consts.SOLDIER_PIXALES,
    ],
    "night_soldier": [
        pygame.image.load(consts.NIGHT_SOLDIER_PATH),
        consts.SOLDIER_SIZE,
        consts.SOLDIER,
        consts.SOLDIER_PIXALES,
    ],
    "guard": [
        pygame.image.load(consts.SNAKE_PATH),
        consts.SOLDIER_SIZE,
        6,
        consts.SOLDIER_PIXALES,
    ],
}

x_ray_object = ["mine", "night_soldier"]
always_visible=["flag","guard"]
mobs = ["soldier", "night_soldier", "guard"]



def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_welcome():
    draw_message(
        consts.WELCOME_MESSAGE,
        consts.WELCOME_FONT_SIZE,
        consts.WELCOME_COLOR,
        consts.WELCOME_LOCATION,
    )


def draw_load_game(game_number):
    draw_message(
        consts.LOAD_GAME_MESSAGE + str(game_number),
        consts.LOAD_MSG_FONT,
        consts.WIN_COLOR,
        consts.LOAD_LOCATION,
    )


def draw_save_game(game_number):
    print(game_number)
    draw_message(
        consts.SAVE_GAME_MESSAFE + str(game_number),
        consts.LOAD_MSG_FONT,
        consts.WIN_COLOR,
        consts.LOAD_LOCATION,
    )


def draw_image(obj_info, field):
    loaded_img, size, object_index, object_pixales = obj_info
    img = loaded_img
    img = pygame.transform.scale(img, size)
    count_pixales = 0
    for row in range(consts.BOARD_GRID_ROW):
        for col in range(consts.BOARD_GRID_COLS):

            if field[row][col] == object_index:
                if count_pixales == 0:
                    screen.blit(img, (col * consts.BLOCK_SIZE, row * consts.BLOCK_SIZE))
                    count_pixales = object_pixales
                count_pixales -= 1




def draw_dead(field,state):
    photos=[pygame.image.load(consts.BANG_PATH),pygame.image.load(consts.SOLDIER_DEATH_PATH)]
    print(state["object_hitted"])
    for i in range(len(photos)):
        if not(state["object_hitted"] == consts.GUARD and i==0):
            draw_image([photos[i],consts.SOLDIER_SIZE,consts.SOLDIER,consts.SOLDIER_PIXALES],field)


def draw_lose_message():

    draw_message(
        consts.LOSE_MESSAGE,
        consts.LOSE_FONT_SIZE,
        consts.LOSE_COLOR,
        consts.LOSE_LOCATION,
    )


def draw_win_message():
    draw_message(
        consts.WIN_MESSAGE, consts.WIN_FONT_SIZE, consts.WIN_COLOR, consts.WIN_LOCATION
    )


def drawGrid():
    # Set the size of the grid block
    screen.fill(consts.BLACK)
    for x in range(0, consts.WINDOW_WIDTH, consts.BLOCK_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.BLOCK_SIZE):
            rect = pygame.Rect(x, y, consts.BLOCK_SIZE, consts.BLOCK_SIZE)
            pygame.draw.rect(screen, consts.GRAY, rect, 1)

def print_by_category(category,field,main_field):
    for name in category:
        if name in mobs:
            draw_image(objects[name], field)
        else:
            draw_image(objects[name], main_field)
def x_ray(field, main_field):
    drawGrid()
    print_by_category(x_ray_object,field,main_field)
    print_by_category(always_visible,field,main_field)
    time.sleep(consts.X_RAY_TIME)


def draw_game(state, field, main_field):
    screen.fill(consts.BACKGROUND_COLOR)

    for name, info in objects.items():
        if name not in x_ray_object:
            if name not in mobs:
                draw_image(info, main_field)
            else:
                draw_image(info, field)


    if state["state"] == consts.SPACE_X_RAY:
        x_ray(field, main_field)
        state["state"] = consts.RUNNING_STATE

    # ============================= states
    if state["state"] == consts.LOSE_STATE:
        x_ray(field,main_field)
        draw_dead(field,state)
        draw_lose_message()
    elif state["state"] == consts.WIN_STATE:
        draw_win_message()
    elif state["state"] == consts.WELCOME_STATE:
        draw_welcome()
    # =============================  load and save
    if state["is_key_load"] == consts.LOAD_STATE:
        draw_load_game(state["what_number_pressed"])
    if state["is_key_load"] == consts.SAVE_STATE:
        draw_save_game(state["what_number_pressed"])




    pygame.display.flip()
