import pytest
from exception import IndianCensusException
from main import census, no_of_records

class TestIndianCensus:
    csv_file='C:/Users/Shubham/Desktop/IndianCensusAnalyzer/IndianCensus - Sheet1.csv'

   def test_no_of_records(self):
        expected= no_of_records()
        assert expected == 29

test1=TestIndianCensus()
print(test1)
