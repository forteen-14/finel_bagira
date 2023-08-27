import consts


# parameters: field
# return: a list of the guard position in the field
# this function return a list of the guard position in the field
def get_guard_position(field):
    gaurd_index_list = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == consts.GUARD:
                gaurd_index_list.append([row, col])
    return gaurd_index_list


# parameters: field, direction
# return: the direction of the guard
# this function move the guard in the field
def move_guard(field, direction):
    guard_position = get_guard_position(field)
    if direction == consts.GUARD_RIGHT:
        if move_guard_right(field, guard_position) == consts.SOLDIER_OUT_OF_BOUNDS:
            direction = consts.GUARD_LEFT
    if direction == consts.GUARD_LEFT:
        if move_guard_left(field, guard_position) == consts.SOLDIER_OUT_OF_BOUNDS:
            direction = consts.GUARD_RIGHT
    return direction


# parameters: field, guard_position
# return: if the guard is out of bounds
# this function move the guard to the right
def move_guard_right(field, guard_position):

    for i in guard_position:
        next_position_info = field[i[0]][i[1] + 1]
        if (
            0 <= i[0] < consts.BOARD_GRID_ROW - consts.GUARD_SPEED
            and 0
            <= i[1] + consts.GUARD_SPEED
            < consts.BOARD_GRID_COLS - consts.GUARD_SPEED
        ):
            field[i[0]][i[1] + consts.GUARD_SPEED] = consts.GUARD
            field[i[0]][i[1]] = consts.EMPTY
        else:
            return consts.SOLDIER_OUT_OF_BOUNDS


# parameters: field, guard_position
# return: true if the guard hit the soldier
# this function check if the guard hit the soldier
def isHitSolider(field, guard_position, direction):
    print(*field,sep="\n")
    print("\n\n\n")
    step = consts.GUARD_SPEED
    if direction == consts.GUARD_LEFT:
        step = -1*consts.GUARD_SPEED
    for position in guard_position:
        if field[position[0]][position[1] + step] == consts.SOLDIER:
            return True
    return False


# parameters: field, guard_position
# return: if the guard is out of bounds
# this function move the guard to the left
def move_guard_left(field, guard_position):
    for i in guard_position:
        next_position_info = field[i[0]][i[1] - 1]
        if (
            0 <= i[0] < consts.BOARD_GRID_ROW
            and 0 <= i[1] - consts.GUARD_SPEED < consts.BOARD_GRID_COLS
        ):
            field[i[0]][i[1] - consts.GUARD_SPEED] = consts.GUARD
        else:
            return consts.SOLDIER_OUT_OF_BOUNDS
    for i in guard_position:
        field[i[0]][i[1]] = consts.EMPTY


# parameters: state, field, direction
# return: Guard status
# this function update the guard status
def update_guard_status(state, field, direction):
    # if isHitSolider(field, get_guard_position(field), direction):
    #     state["state"] = consts.LOSE_STATE
    #     return
    state["guard_Direction"] = move_guard(field, direction)
    state["object_hitted"]=consts.GUARD
