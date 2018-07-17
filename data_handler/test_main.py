from modules.phay_mods import *

TEST_FILE = "data_sources/sf_restaurant_scores_subset.csv"

def test_read_file():
	data = analuze.read_file(TEST_FILE)

	assert len(data) == 100
	assert len(data[0].keys()) == 17