from modules.phay_mods import *

TEST_FILE = "data_sources/sf_restaurant_subset.csv"

def test_read_file():
	data = read_file(TEST_FILE)

	assert len(data) == 100
	assert len(data[0].keys()) == 17

def test_filter_inspection_type():
	data = [
		{'inspection_type' : 'A'},
		{'inspection_type' : 'B'},
		{'inspection_type' : 'C'},
		{'inspection_type' : 'A'}
	]

	assert filter_inspection_type(data, 'A') == [
		{'inspection_type' : 'A'}, {'inspection_type' : 'A'}]
	assert filter_inspection_type(data, 'B') == [
		{'inspection_type' : 'B'}]

	#edge case
	assert filter_inspection_type([], 'A') == []
	assert filter_inspection_type(data, 'Z') == []

