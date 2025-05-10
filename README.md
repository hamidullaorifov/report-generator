# Report Generation System

This project provides a script to generate reports based on CSV input files. It supports only `payout` report for now, which calculates the payout based on employee rates and hours worked.

## Setup

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/hamidullaorifov/report-generator.git
cd report-generator
```

### 2. Install dependencies
Install the required Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Running the script
### 1. Run the Report Generation Script
The main script main.py accepts the following arguments:

- files: One or more CSV file paths containing employee data (required).

- --report: The type of report to generate (required). Options include payout.

- --output: The output file path to save the generated report (optional, default: output/reports.json).

Example command to generate a payout report:
```bash
python main.py data1.csv data2.csv --report payout --output output/reports.json
```
This will generate output/reports.json file
![image](https://github.com/user-attachments/assets/fcb55871-6663-4955-822c-c9825315a29a)

### 2.Run tests and see coverage report
Command to run tests
```bash
pytest --cov=.
```
It displays coverage report
![image](https://github.com/user-attachments/assets/42cd7e9a-3ee0-436f-a7a8-6907f104156f)



