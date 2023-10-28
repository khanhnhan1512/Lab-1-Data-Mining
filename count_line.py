from main import *

def count_line_with_missing_values(data) -> int:
    index_empty_row = set()
    for feature in data.keys():
        for index,value in enumerate(data[feature]):
            if is_nan(value):
                index_empty_row.add(index)
    return len(index_empty_row)

def main():
    arguments = parse_cmd()
    filename = arguments[0].split('=')[1]
    data = read_file(filename)
    print(f"There are total {count_line_with_missing_values(data)} lines with missing values")
    
if __name__ == '__main__':
    main()