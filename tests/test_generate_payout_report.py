import pytest
from reports.payout_report import generate_payout_report
from parsers.csv_parser import parse_csv


def test_valid_dataset():
	data = [
		{'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'rate': '45'},
		{'department': 'Marketing', 'id': '102', 'email': 'henry@example.com', 'name': 'Henry Martin', 'hours_worked': '150', 'rate': '35'},
		{'department': 'HR', 'id': '103', 'email': 'ivy@example.com', 'name': 'Ivy Clark', 'hours_worked': '158', 'rate': '38'},
	]

	expected_report = {
		'Marketing': {
			'employees': [
				{'name': 'Henry Martin', 'hours': 150, 'rate': 35, 'payout': 5250}
			],
			'total_hours': 150,
			'total_payout': 5250
		},
		'HR': {
			'employees': [
				{'name': 'Grace Lee', 'hours': 160, 'rate': 45, 'payout': 7200},
				{'name': 'Ivy Clark', 'hours': 158, 'rate': 38, 'payout': 6004},
			],
			'total_hours': 318,
			'total_payout': 13204
		}
	}

	result = generate_payout_report(data)

	assert expected_report == result


def test_single_employee_in_department():
	data = [
		{'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'rate': '45'},
	]

	expected_report = {
		'HR': {
			'employees': [
				{'name': 'Grace Lee', 'hours': 160, 'rate': 45, 'payout': 7200},
			],
			'total_hours': 160,
			'total_payout': 7200
		}
	}

	result = generate_payout_report(data)

	assert expected_report == result

def test_single_employee_in_department():
	data = [
		{'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'rate': '45'},
	]

	expected_report = {
		'HR': {
			'employees': [
				{'name': 'Grace Lee', 'hours': 160, 'rate': 45, 'payout': 7200},
			],
			'total_hours': 160,
			'total_payout': 7200
		}
	}

	result = generate_payout_report(data)

	assert expected_report == result

def test_multiple_employees_multiple_departments():
	data = [
		{'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'rate': '45'},
		{'department': 'Marketing', 'id': '102', 'email': 'henry@example.com', 'name': 'Henry Martin', 'hours_worked': '150', 'rate': '35'},
		{'department': 'HR', 'id': '103', 'email': 'ivy@example.com', 'name': 'Ivy Clark', 'hours_worked': '158', 'rate': '38'},
		{'department': 'Marketing', 'id': '104', 'email': 'john@example.com', 'name': 'John Doe', 'hours_worked': '50', 'rate': '40'},
	]

	expected_report = {
		'Marketing': {
			'employees': [
				{'name': 'Henry Martin', 'hours': 150, 'rate': 35, 'payout': 5250},
				{'name': 'John Doe', 'hours': 50, 'rate': 40, 'payout': 2000},
			],
			'total_hours': 200,
			'total_payout': 7250
		},
		'HR': {
			'employees': [
				{'name': 'Grace Lee', 'hours': 160, 'rate': 45, 'payout': 7200},
				{'name': 'Ivy Clark', 'hours': 158, 'rate': 38, 'payout': 6004},
			],
			'total_hours': 318,
			'total_payout': 13204
		}
	}

	result = generate_payout_report(data)

	assert expected_report == result

def test_zero_hours():
	data = [
		{'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '0', 'rate': '45'},
		{'department': 'Marketing', 'id': '102', 'email': 'henry@example.com', 'name': 'Henry Martin', 'hours_worked': '0', 'rate': '35'},
		{'department': 'HR', 'id': '103', 'email': 'ivy@example.com', 'name': 'Ivy Clark', 'hours_worked': '158', 'rate': '38'},
	]

	expected_report = {
		'Marketing': {
			'employees': [
				{'name': 'Henry Martin', 'hours': 0, 'rate': 35, 'payout': 0}
			],
			'total_hours': 0,
			'total_payout': 0
		},
		'HR': {
			'employees': [
				{'name': 'Grace Lee', 'hours': 0, 'rate': 45, 'payout': 0},
				{'name': 'Ivy Clark', 'hours': 158, 'rate': 38, 'payout': 6004},
			],
			'total_hours': 158,
			'total_payout': 6004
		}
	}

	result = generate_payout_report(data)

	assert expected_report == result

def test_empty_data():
	data = []
	expected_report = {}

	result = generate_payout_report(data)
	assert result == expected_report


def test_generate_report_from_csv():
	file_path = 'tests/data/employee_rate.csv'
	data = parse_csv(file_path)

	expected_report = {
		'Marketing': {
			'employees': [
				{'name': 'Henry Martin', 'hours': 150, 'rate': 35, 'payout': 5250}
			],
			'total_hours': 150,
			'total_payout': 5250
		},
		'HR': {
			'employees': [
				{'name': 'Grace Lee', 'hours': 160, 'rate': 45, 'payout': 7200},
				{'name': 'Ivy Clark', 'hours': 158, 'rate': 38, 'payout': 6004},
			],
			'total_hours': 318,
			'total_payout': 13204
		}
	}

	result = generate_payout_report(data)

	assert expected_report == result

