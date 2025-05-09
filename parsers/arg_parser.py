import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('files', nargs='+', help="Paths to input csv files.")
	parser.add_argument('--report', required=True, help="Name of the report")

	return parser.parse_args()