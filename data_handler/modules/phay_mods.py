"""
Utilities for working with SF restaurant data.

"""

def read_file(filename):
	"""
	Read a CSV file of San Francisco public city restaurant inspection data.
	--https://data.sfgov.org/Health-and-Social-Services/Restaurant-Scores-LIVES-Standard/pyih-qa8l/data
	

	Returns list of dictionaries with one dictionary per row of the file.
	"""

def filter_inspection_type(data, inspection_type):
	"""
	Filter data to only include rows with a given inspection type
	"""



def filter_month(data, month, year):
	"""
	Filter data to only include rows from a given month.

	could use an API...

	Returns a list of filtered data.
	"""


def count_risk_categories(data):
	"""
	Count the number of each risk category in a given dataset.

	Returns dictionary pairing a risk caetegory with a number of occurences.
	"""

def count_risk_categories_by_month(data, month, year):
	"""
	Count the number of risk categories in a given month.

	
	"""
