# drop url columns from data.csv file
# author -- Eric Liu

import pandas as pd
data = pd.read_csv('data.csv') ## original FIFA19 dataset

## beginning match function
def startswith(char, start):
    if isinstance(char, type("str")): ## check if this column contains str type
        if len(char) > len(start) and char[:len(start)] == start:
            return True
        else:
            return False
    else:
        return False

## url columns drop function
def drop_url(dataframe):
    columns = data.columns
    for col in columns:
        if startswith(dataframe[[col]].iloc[0,0], "https://"):
            dataframe.drop(columns=[col], inplace=True)

## utlize drop_url function on data.csv
drop_url(data)
if 'Unnamed: 0' in data.columns:
    data.drop(columns=['Unnamed: 0'], inplace=True)

## save modified dataset as data_nourl
data_nourl = data.to_csv('data_nourl.csv', index = True)