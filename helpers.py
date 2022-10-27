import pandas as pd
import os

def load_dataset(name):
    cwd = os.getcwd()
    print(cwd)
    os.chdir(os.path.dirname(cwd))
    fName = f'__datasets\{name}.csv'
    df = pd.read_csv(fName)
    os.chdir(cwd)
    print(df.shape)
    print(df.info())
    return df