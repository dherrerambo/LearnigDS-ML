import pandas as pd
import os

def load_dataset(name:str, debug:bool=False):
    cwd = os.getcwd()
    if debug==True: print(cwd)
    os.chdir(os.path.dirname(cwd))
    fName = f'datasets/{name}.csv'
    df = pd.read_csv(fName)
    os.chdir(cwd)
    print(f"{df.shape}=")
    print(df.info())
    return df