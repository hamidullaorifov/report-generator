import sys
from parsers.csv_parser import parse_csv
from parsers.arg_parser import parse_args
from reports.payout_report import generate_payout_report
from utils.utils import write_json_report, load_data


REPORT_GENERATORS = {
	'payout': generate_payout_report,
}

def main():
	args = parse_args()
	if args.report not in REPORT_GENERATORS:
		print("This error type is not supported")
		sys.exit(1)
	try:
		data = load_data(args.files)
		report_func = REPORT_GENERATORS[args.report]
		report = report_func(data)
		write_json_report(report, 'output/report.json')
	except Exception as e:
		print(f"Failed to generate report: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()

	

