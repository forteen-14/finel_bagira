import pandas as pd
import consts
import os

df = pd.DataFrame()

def DataBase():
    global df
    if os.path.exists(f'./{consts.DB_NAME_PATH}'):
        data = pd.read_csv(consts.DB_NAME_PATH)
        df = pd.DataFrame(data)
    return df

def SaveGame(key_pressed,field):
    df[str(key_pressed)]=field
    df.to_csv(consts.DB_NAME_PATH, index=False)


def loadGame(key_pressed):
    print(key_pressed)
    return df.get(key_pressed).values




