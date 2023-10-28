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
    for feature in index_missing.keys():
        if len(index_missing[feature]) >= limit_number:
            data.pop(feature)

def main():
    data = read_file('house-prices.csv')
    delete_column(data, 500)
    create_csv_file('result.csv', data)
    
if __name__ == '__main__':
    main()