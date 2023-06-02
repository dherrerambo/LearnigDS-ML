import pandas as pd
import os

def load_dataset(name:str, debug:bool=False):
    cwd = os.getcwd()
    cwd = os.path.dirname(cwd)
    fName = fr'{cwd}\datasets\{name}'
    try:
        df = pd.read_csv(fName+".csv.gz")
    except:
        df = pd.read_csv(fName+".csv")
    if debug==False: print(f"{df.shape=}")
    if debug==True: print(df.info())
    return df