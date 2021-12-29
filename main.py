import pandas as pd

def census():
    '''
    Adding data from csv file
    '''
    csv=pd.read_csv('C:/Users/Shubham/Desktop/IndianCensusAnalyzer/IndianCensus - Sheet1.csv')
    return csv


def no_of_records():
    '''Finding number of records(no of rows and columns) in csv file'''
    csv=census()
    return csv.shape[0]

data2=no_of_records()

