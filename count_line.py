from main import *

def count_line_with_missing_values(data) -> int:
    index_empty_row = set()
    for feature in data.keys():
        for index,value in enumerate(data[feature]):
            if is_nan(value):
                index_empty_row.add(index)
    return len(index_empty_row)

def main():
    data = read_file('house-prices.csv')
    print(f"There are {count_line_with_missing_values(data)} lines with missing values")
    
if __name__ == '__main__':
    main()