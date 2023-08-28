import pandas as pd
import consts
import os

df = pd.DataFrame()

# parameters: key
# return: True if the key is in the data base, False otherwise
# this function checks if the key is in the data base
def isKeyExist(key):
    return key in df.keys()


# parameters: None
# return: None
# this function loads the data base
def DataBase():
    global df
    if os.path.exists(f"./{consts.DB_NAME_PATH}"):
        df = pd.read_pickle(consts.DB_NAME_PATH)


# parameters: key_pressed, field, field_copy
# return: None
# this function saves the game in the data base
def SaveGame(key_pressed, field, field_copy):
    df[str(key_pressed)] = [field, field_copy]
    df.to_pickle(consts.DB_NAME_PATH)


# parameters: key_pressed
# return: the key in which the game is saved in the data base
# this function loads the game from the data base
def loadGame(key_pressed):
    if isKeyExist(key_pressed):
        return df[key_pressed].values.tolist()
    return None,None
