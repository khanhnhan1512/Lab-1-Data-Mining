from main import *

# Find the columns with missing values greater than a particular number and delete them
def delete_column(data, limit_number):
    # Determine the missing values for each column
    index_missing = {}
    for feature in data.keys():
        index_missing[feature] = []
        for i, value in enumerate(data[feature]):
            if is_nan(value):
                index_missing[feature].append(i)
    # Remove the column has the number of missing values greater than a particular number
    count = 0
    for feature in index_missing.keys():
        if len(index_missing[feature]) >= limit_number:
            count += 1
            data.pop(feature)
    print(f'{count} columns have been deleted')

def main():
    arguments = parse_cmd()
    filename = arguments[0].split('=')[1]
    limit_number = int(arguments[1].split('=')[1])
    filename_out = arguments[2].split('=')[1]
    data = read_file(filename)
    delete_column(data, limit_number)
    create_csv_file(filename_out, data)
    
if __name__ == '__main__':
    main()