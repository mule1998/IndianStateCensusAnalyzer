import pandas as pd
import csv
from csv import Dialect
from exception import IndianStatesCensusException


class IndianStateCensus:

    def state_census_problem(self, file_name):
        """This function is for read the csv data"""
        csv_data = pd.read_csv(file_name)
        return csv_data

    def count_records(self, file_name):
        """This function is for the find shape of the data."""
        csv_data = self.state_census_problem(file_name)
        return csv_data.shape[0]

    def file_correct(self, file_name):
        """function checking file extension"""
        csv_data = open(file_name)
        if csv_data.name.endswith(".csv"):
            return file_name
        else:
            raise IndianStatesCensusException("Invalid file name")

    def delimiter_validation(self, file_name):
        """in this function we are using delimiter and check how we separate values"""
        with open(file_name, newline="") as file_data:
            dialect = csv.Sniffer().sniff(file_data.read())
            if not dialect.delimiter == ',':
                raise IndianStatesCensusException("Error occurred")
            else:
                return dialect.delimiter

    def header_validate(self, file_name):
        """In this function we are checking header of the file"""
        with open(file_name, newline="") as file_data:
            dialect = csv.Sniffer().has_header(file_data.read())
            if not dialect:
                raise IndianStatesCensusException("Heading corrupt")
            else:
                return dialect


if __name__ == '__main__':
    data2 = IndianStateCensus()
    print(data2.count_records("IndianCensus - Sheet1.csv"))
    print(data2.file_correct("IndianCensus - Sheet1.csv"))
    print(data2.delimiter_validation("IndianCensus - Sheet1.csv"))
    print(data2.header_validate("IndianCensus - Sheet1.csv"))
