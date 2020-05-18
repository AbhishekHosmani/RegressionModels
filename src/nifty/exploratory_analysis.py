import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from scipy import stats


def data_cleaning(df):
    #Checking for null values
    missing_cnt = df.isnull().sum()
    if missing_cnt.sum() == 0:
        print("No missing values in dateset")
        return
    else:
        for column in df.columns:
            print("Columns {} has type {}".format(column, df[column].dtypes))
            # if np.issubdtype(df[column].dtype, np.number):               
            #     print("{} is a numeric variable".format(column))
            # else:
            #     print("{} is a categorical variable".format(column))

def main():
    data_source = './../../data/nifty/'
    data_files = os.listdir(data_source)
    missing_values = ["n/a", "na", "--"]
    try:
        print("Datasets Found:", data_files)
        for data in data_files:

            if not data.endswith(".csv"):
                continue
            df = pd.read_csv(data_source+data, na_values=missing_values)
            print("DATASET" + data)
            print(df.info())
            data_cleaning(df)
    except Exception as e:
        print("ERROR:   ", e)


if __name__ == "__main__":
    main()


    

