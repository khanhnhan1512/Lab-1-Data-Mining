import pandas as pd
import csv
import sys

# Read the data from the file
def read_file(filename) -> dict:
    df = pd.read_csv(filename)
    data = df.to_dict(orient='list')
    return data
# Check if the value is nan
def is_nan(value) -> bool:
    return (value != value)
# save the new data to csv file
def create_csv_file(file_name, dict) -> None:
    column_names = list(dict.keys())
    rows = zip(*dict.values())
    # convert nan value to empty string
    rows = [[value if not is_nan(value) else '' for value in row] for row in rows]
    # write to csv file
    with open(file_name, 'w', newline='') as f:
        pen = csv.writer(f)
        pen.writerow(column_names)
        pen.writerows(rows)
    print(f'The output file is {file_name}')
# get all the arguments from the command line
def parse_cmd() -> list:
    n = len(sys.argv)
    return sys.argv[1:n]

        