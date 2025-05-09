from typing import List, Dict, Any
from collections import defaultdict


def generate_payout_report(data: List[Dict[str, Any]]) -> Dict[str, Any]:

	report: Dict[str, Any] = {}

	grouped = defaultdict(list)

	if not data:
		return report

	for item in data:
		department = item['department']
		name = item['name']
		rate = int(item['rate'])
		hours = int(item['hours_worked'])
		payout = hours * rate

		grouped[department].append(
			{
				'name': name,
				'hours': hours,
				'rate': rate,
				'payout': payout
			}
		)
	
	for department, employees in grouped.items():
		total_hours = sum(emp['hours'] for emp in employees)
		total_payout = sum(emp['payout'] for emp in employees)

		report[department] = {
			'employees': employees,
			'total_hours': total_hours,
			'total_payout': total_payout
		}
	return report
