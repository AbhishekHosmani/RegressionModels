import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def data_cleaning(df):

    #Checking for null values
    missing_cnt = df.isnull().sum()
    if missing_cnt.sum() == 0:
        print("No missing values in dateset")
        return
    else:
        print(missing_cnt)


if __name__ == "__main__":
    data_source = './../../data/nifty/'
    nifty_50_df = pd.read_csv(data_source + 'NIFTY_50.csv')
    nifty_100_df = pd.read_csv(data_source + 'NIFTY_100.csv')
    nifty_bank_df = pd.read_csv(data_source + 'NIFTY_BANK.csv')
    print(nifty_bank_df.head)
    

