import os
import json
import pytest
import tempfile

from utils.report_utils import write_json_report, load_data

def test_write_to_json_creates_file():
	data = {
		'Marketing': {
			'employees': [
				{'name': 'Henry Martin', 'hours': 150, 'rate': 35, 'payout': 5250},
				{'name': 'John Doe', 'hours': 50, 'rate': 40, 'payout': 2000},
			],
			'total_hours': 200,
			'total_payout': 7250
		}
	}
	with tempfile.TemporaryDirectory() as tmpdir:
		output_path = os.path.join(tmpdir, 'reports', 'report.json')

		write_json_report(data, output_path)

		assert os.path.exists(output_path)

		with open(output_path, 'r', encoding='utf-8') as file:
			content = json.load(file)
			assert content == data

file_sets_with_expected_counts = [
	(['tests/data/employee_rate.csv'], 3),
	(['tests/data/employee_rate.csv', 'tests/data/employee_hourly_rate.csv'], 6),
	(['tests/data/employee_rate.csv', 'tests/data/employee_hourly_rate.csv', 'tests/data/employee_salary.csv'],9),
	(['tests/data/employee_rate.csv', 'tests/data/employee_no_rows.csv'],3)
]

@pytest.mark.parametrize(('files', 'count'), file_sets_with_expected_counts)
def test_load_data(files, count):
	data = load_data(files)

	assert len(data) == count
