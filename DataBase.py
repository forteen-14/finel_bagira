import pandas as pd
import consts
df = pd.DataFrame()

def SaveGameToDataBase(key_pressed,field):
    df[str(key_pressed)]=field

def loadGame(key_pressed):
    return df[str(key_pressed)]

def SaveDataBaseOnComputer():
    df.to_csv(consts.DB_NAME_PATH, index=False)

def loadDataBase():
    global df
    df=pd.read_csv(consts.DB_NAME_PATH)