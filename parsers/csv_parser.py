from typing import List, Dict, Any


def parse_csv(file_path: str) -> List[Dict[str, Any]]:
	rows: List[Dict[str, str]] = []

	with open(file_path, 'r', encoding='utf-8') as file:
		lines = file.readlines()
		
		if not lines:
			return []
		
		headers = lines[0].strip().split(',')
		headers = [header.strip() for header in headers]
		for i, header in enumerate(headers):
			if header in ['rate', 'hourly_rate', 'salary']:
				headers[i] = 'rate'

		for line in lines[1:]:
			values = line.strip().split(',')
			
			if len(values) != len(headers):
				continue

			row = {
				header: value.strip() for header, value in zip(headers, values)
			}

			rows.append(row)

	return rows

		