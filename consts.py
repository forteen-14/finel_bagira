GAME_NAME = "The Flag"
WELCOME_STATE=0
RUNNING_STATE=1
LOSE_STATE=2
WIN_STATE=3
SPACE_X_RAY = 4
GRAY=(50,50,50)
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
WELCOME_FONT_SIZE=int(0.1 * WINDOW_WIDTH)
WELCOME_COLOR=WHITE
WELCOME_LOCATION=(0.04 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WELCOME_FONT_SIZE / 2))


GRASS_AMOUNT = 20
MINES_AMOUNT = 20


SOLDIER_HIGHT = 4
SOLDIER_WIDTH = 2


SOLDIER_MINE_HIT = "hit mine"
SOLDIER_FLAG_HIT = "win"
SOLDIER_OUT_OF_BOUNDS = "out of bounds"
SOLDIER_MOVE = "move"

GRASS = 2
EMPTY = 0
SOLDIER = 3
MINE = 1
FLAG = 4

SOLIDER_PNG_PATH="rec/soldier.png"
MINE_PNG_PATH = "rec/mine.png"
BUSH_PNG_PATH="rec/grass.png"
FLAG_PNG_PATH="rec/flag.png"
DIFFERENT_OBJECT_COUNT=4

SOLIDER_WIDTH=2*BLOCK_SIZE
SOLIDER_HEIGHT=4*BLOCK_SIZE
SOLDIER_START_POINT=(0,0)
SOLDIER_SIZE=(SOLIDER_WIDTH,SOLIDER_HEIGHT)


MINE_WIDTH=3*BLOCK_SIZE
MINE_HEIGHT=1*BLOCK_SIZE
MINE_SIZE=(MINE_WIDTH,MINE_HEIGHT)

BUSH_WIDTH=1*BLOCK_SIZE
BUSH_HEIGHT=1*BLOCK_SIZE
BUSH_SIZE=(BUSH_WIDTH,BUSH_HEIGHT)

FLAG_WIDTH=3*BLOCK_SIZE
FLAG_HEIGHT=4*BLOCK_SIZE
FLAG_SIZE=(FLAG_WIDTH,FLAG_HEIGHT)

FLAG_START_POINT=(0,0)


SOLDIER_DEATH_PATH="rec/injury.png"
BANG_PATH="rec/explotion.png"

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = WHITE
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = LOSE_COLOR
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

