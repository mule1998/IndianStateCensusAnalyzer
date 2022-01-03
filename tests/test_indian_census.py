import pytest
from exception import IndianStatesCensusException
from main import IndianStateCensus


class TestIndianStateCensusProblem:
    csv_file = 'C:/Users/Shubham/Desktop/IndianCensusAnalyzer/IndianCensus - Sheet1.csv'
    wrong_file_extension= '../IndianCensus - Sheet1.txt'

    @pytest.fixture()
    def test_indian_states_census(self):
        data = IndianStateCensus()
        return data

    def test_match_records(self, test_indian_states_census):
        expected = test_indian_states_census.count_records(self.csv_file)
        assert expected == 29

    def test_file_correct(self, test_indian_states_census):
        expected = self.file_correct
        result = test_indian_states_census.check_file_extension(self.file_correct)
        assert result == expected

    def test_not_path_file_correct(self, test_indian_states_census):
        expected = "Invalid file name"
        with pytest.raises(IndianStatesCensusException) as exception:
            test_indian_states_census.check_file_extension(self.wrong_file_extension)
            assert exception.value.message == expected

    def test_delimiter_validation(self, test_indian_states_census):
        expected = ','
        result = test_indian_states_census.delimiter_validation(self.csv_file)
        assert result == expected

    def test_not_match_delimiter(self, test_indian_states_census):
        expected = "Error occurred"
        with pytest.raises(IndianStatesCensusException) as exception:
            test_indian_states_census.delimiter_validation(self.wrong_file_extension)
        assert exception.value.message == expected

    def test_header_validate(self, test_indian_states_census):
        expected = True
        result = test_indian_states_census.header_validate(self.csv_file)
        assert result == expected

    def test_not_match_header(self, test_indian_states_census):
        expected = "Heading corrupt"
        with pytest.raises(IndianStatesCensusException) as exception:
            test_indian_states_census.header_validate(self.wrong_file_extension)
        assert exception.value.message == expected
