import consts


def get_guard_position(field):
    gaurd_index_list = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == consts.GUARD:
                gaurd_index_list.append([row, col])
    return gaurd_index_list


def move_guard(field, direction):
    guard_position = get_guard_position(field)
    if direction == consts.GUARD_RIGHT:
        if move_guard_right(field, guard_position) == consts.SOLDIER_OUT_OF_BOUNDS:
            direction = consts.GUARD_LEFT
    if direction == consts.GUARD_LEFT:
        if move_guard_left(field, guard_position) == consts.SOLDIER_OUT_OF_BOUNDS:
            direction = consts.GUARD_RIGHT
    return direction



def move_guard_right(field, guard_position):

    for i in guard_position:
        next_position_info = field[i[0]][i[1]+1]
        if 0 <= i[0] < consts.BOARD_GRID_ROW-consts.GUARD_SPEED and 0 <= i[1] + consts.GUARD_SPEED < consts.BOARD_GRID_COLS-consts.GUARD_SPEED:
            field[i[0]][i[1] + consts.GUARD_SPEED] = consts.GUARD
            field[i[0]][i[1]] = consts.EMPTY
        else:
            return consts.SOLDIER_OUT_OF_BOUNDS

def isHitSolider(field, guard_position,direction):
    step=1
    if direction==consts.GUARD_LEFT:
        step=-1
    for position in guard_position:
        if field[position[0]][position[1]+step]==consts.SOLDIER:
            return True
        return False





def move_guard_left(field, guard_position):
    for i in guard_position:
        next_position_info = field[i[0]][i[1]-1]
        if 0 <= i[0] < consts.BOARD_GRID_ROW and 0 <= i[1] - consts.GUARD_SPEED < consts.BOARD_GRID_COLS:
            field[i[0]][i[1] - consts.GUARD_SPEED] = consts.GUARD
        else:
            return consts.SOLDIER_OUT_OF_BOUNDS
    for i in guard_position:
        field[i[0]][i[1]] = consts.EMPTY

def update_guard_status(state,field,direction):
    if isHitSolider(field,get_guard_position(field),direction):
        state["state"]=consts.LOSE_STATE
        return
    state["guard_Direction"]=move_guard(field,direction)
