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


GRASS_AMOUNT = 200
MINES_AMOUNT = 20
TELEPORT_AMOUNT = 5

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
TELEPORT = 5

SOLIDER_PNG_PATH="rec/soldier.png"
MINE_PNG_PATH = "rec/mine.png"
BUSH_PNG_PATH="rec/grass.png"
FLAG_PNG_PATH="rec/flag.png"
NIGHT_SOLDIER_PATH="rec/soldier_nigth.png"
SOLDIER_DEATH_PATH="rec/injury.png"
BANG_PATH="rec/explotion.png"
SNAKE_PATH="rec/snake.png"
DIFFERENT_OBJECT_COUNT=4

SOLIDER_WIDTH=2*BLOCK_SIZE
SOLIDER_HEIGHT=4*BLOCK_SIZE
SOLDIER_START_POINT=(0,0)
SOLDIER_SIZE=(SOLIDER_WIDTH,SOLIDER_HEIGHT)
SOLDIER_PIXALES=8


MINE_WIDTH=3*BLOCK_SIZE
MINE_HEIGHT=1*BLOCK_SIZE
MINE_SIZE=(MINE_WIDTH,MINE_HEIGHT)
MINE_PIXALES=3

BUSH_WIDTH=1*BLOCK_SIZE
BUSH_HEIGHT=1*BLOCK_SIZE
BUSH_SIZE=(BUSH_WIDTH,BUSH_HEIGHT)
BUSH_PIXALES=1

FLAG_WIDTH=3*BLOCK_SIZE
FLAG_HEIGHT=4*BLOCK_SIZE
FLAG_SIZE=(FLAG_WIDTH,FLAG_HEIGHT)
FLAG_PIXALES=12

TP_PIXALES = 3
TP_WIDTH = 3 * BLOCK_SIZE
TP_HEIGHT = 1 * BLOCK_SIZE
TP_SIZE = (TP_WIDTH, TP_HEIGHT)






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
TIME_DELAY=3
X_RAY_TIME=1

LOAD_MSG_FONT=int(0.1 * WINDOW_WIDTH)
LOAD_LOCATION=(0.1 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
LOAD_GAME_MSG_TIME=2
SHOW_ON_XRAY="mine"





LOAD_STATE = 0
SAVE_STATE = 1
NEUTRAL_STATE = 2

DB_NAME_PATH="saveGames.pkl"

LOAD_GAME_MESSAGE="loading game: "
SAVE_GAME_MESSAFE="Saving game at: "
DEFAULT_KEY_LOAD_AND_SAVE= " "