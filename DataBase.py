import pandas as pd
import consts
import os

df = pd.DataFrame()

def DataBase():
    global df
    if os.path.exists(f'./{consts.DB_NAME_PATH}'):
        df = pd.read_pickle(consts.DB_NAME_PATH)



def SaveGame(key_pressed,field,field_copy):
    df[str(key_pressed)]=[field,field_copy]
    df.to_pickle(consts.DB_NAME_PATH)



def loadGame(key_pressed):
    return df[key_pressed].values.tolist()




