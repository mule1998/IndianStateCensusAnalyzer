import pytest
from exception import IndianStatesCensusException
from main import state_census_problem,count_records


class TestIndianStateCensusProblem:
    csv_file = '../IndianCensus - Sheet1.csv'

    @pytest.fixture()
    def test_indian_states_census(self):
        data = state_census_problem(self.csv_file)
        return data

    def test_match_records(self):
        expected = count_records(self.csv_file)
        assert expected == 29

