import pandas as pd
import csv


def read_file(filename):
    df = pd.read_csv(filename)
    data = df.to_dict(orient='list')
    return data

def is_nan(value) -> bool:
    return (value != value)

def create_csv_file(file_name, dict):
    column_names = list(dict.keys())
    rows = zip(*dict.values())
    with open(file_name, 'w', newline='') as f:
        pen = csv.writer(f)
        pen.writerow(column_names)
        pen.writerows(rows)