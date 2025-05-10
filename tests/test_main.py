import pytest
import os
import sys
from unittest.mock import MagicMock, patch
from tempfile import TemporaryDirectory
from main import main

def test_main_success(monkeypatch):

	with TemporaryDirectory() as tmp_dir:
		output_path = os.path.join(tmp_dir, 'output/report.json')
		test_args = [
			'main.py',
			'tests/data/employee_rate.csv',
			'--report', 'payout',
			'--output', output_path
		]
		monkeypatch.setattr(sys, 'argv', test_args)

		main()

		assert os.path.exists(output_path)


def test_main_multiple_files(monkeypatch):

	with TemporaryDirectory() as tmp_dir:
		output_path = os.path.join(tmp_dir, 'output/report.json')
		test_args = [
			'main.py',
			'tests/data/employee_rate.csv',
			'tests/data/employee_hourly_rate.csv',
			'tests/data/employee_salary.csv',
			'--report', 'payout',
			'--output', output_path
		]
		monkeypatch.setattr(sys, 'argv', test_args)

		main()

		assert os.path.exists(output_path)

def test_main_unsupported_report(monkeypatch, capsys):
	test_args = [
		'main.py',
		'tests/data/employee_rate.csv',
		'--report', 'invalid',
	]
	monkeypatch.setattr(sys, 'argv', test_args)

	with pytest.raises(SystemExit) as e:
		main()
	captured = capsys.readouterr()
	assert "This error type is not supported" in captured.out
	assert e.value.code == 1