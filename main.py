import pandas as pd


def state_census_problem(file_name):
    """This function is for read the csv data"""
    csv_data = pd.read_csv(file_name)
    return csv_data


def count_records(file_name):
    """This function is for the find shape of the data."""
    csv_data = state_census_problem(file_name)
    return csv_data.shape[0]


data2 = count_records("IndianCensus - Sheet1.csv")
print(data2)
