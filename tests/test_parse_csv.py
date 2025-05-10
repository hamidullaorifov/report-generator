import pytest
from parsers.csv_parser import parse_csv


@pytest.mark.parametrize(('file_name', 'number_of_rows'), [
	('employee_rate.csv', 3),
	('employee_hourly_rate.csv', 3),
	('employee_salary.csv', 3)
	])
def test_rate_column_variants(file_name, number_of_rows):
	file_path = f'tests/data/{file_name}'
	result = parse_csv(file_path)

	for row in result:
		assert 'rate' in row
		assert len(row.keys()) == 6
	assert len(result) == number_of_rows

@pytest.mark.parametrize('file_name', ['employee_empty.csv', 'employee_no_rows.csv'])
def test_empty_csv(file_name):
	file_path = f'tests/data/{file_name}'
	result = parse_csv(file_path)

	assert result == []

def test_inconsistent_data():
	file_path = f'tests/data/inconsistent_data.csv'
	result = parse_csv(file_path)

	expected = [{
		'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'rate': '45'
	}]

	assert result == expected

def test_valid_csv():
	file_path = f'tests/data/employee_rate.csv'
	result = parse_csv(file_path)
	expected = [
		{'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'rate': '45'},
		{'department': 'Marketing', 'id': '102', 'email': 'henry@example.com', 'name': 'Henry Martin', 'hours_worked': '150', 'rate': '35'},
		{'department': 'HR', 'id': '103', 'email': 'ivy@example.com', 'name': 'Ivy Clark', 'hours_worked': '158', 'rate': '38'},
	]

	assert result == expected