import json
import os
from parsers.csv_parser import parse_csv

def write_json_report(report_data, output_path):

	os.makedirs(os.path.dirname(output_path), exist_ok=True)

	with open(output_path, 'w', encoding='utf-8') as file:
		json.dump(report_data, file, indent=4, ensure_ascii=False)

def load_data(files: list[str]) -> list:
	all_data = []
	for file_path in files:
		file_data = parse_csv(file_path)
		all_data.extend(file_data)
	return all_data