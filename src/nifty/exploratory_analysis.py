import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def data_cleaning(df):
    #Checking for null values
    missing_cnt = df.isnull().sum()
    if missing_cnt.sum() == 0:
        print("No missing values in dateset")
        return
    else:
        print(missing_cnt)


def main():
    data_source = './../../data/nifty/'
    data_files = os.listdir(data_source)
    try:
        print("Datasets Found:", data_files)
        for data in data_files:
            if not data.endswith(".csv"):
                continue
            df = pd.read_csv(data_source+data, header=None)
            print("DATASET" + data)
            print(df.head(2))
            data_cleaning(df)
    except Exception as e:
        print("ERROR:   ", e)


if __name__ == "__main__":
    main()


    

