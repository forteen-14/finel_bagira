GAME_NAME = "The Flag"
WELCOME_STATE=0
RUNNING_STATE=1
LOSE_STATE=2
WIN_STATE=3

BOARD_GRID_COLS=50
BOARD_GRID_ROW=25
BLOCK_SIZE=25
WINDOW_HEIGHT = BOARD_GRID_ROW*BLOCK_SIZE
WINDOW_WIDTH = BOARD_GRID_COLS*BLOCK_SIZE
BACKGROUND_COLOR=(0,100,0)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
FONT_NAME="Calibri"
WELCOME_MESSAGE="Welcome to Flag Game"
WELCOME_FONT_SIZE=int(0.15 * WINDOW_WIDTH)
WELCOME_COLOR=WHITE
WELCOME_LOCATION=(0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WELCOME_FONT_SIZE / 2))


GRASS_AMOUNT = 20
MINES_AMOUNT = 20


GRASS = 2
SOLDIER = 3
MINE = 0
FLAG = 1
