from main import *

# Find the rows with missing values for specific column
def index_empty_row(data, column) -> list:
    result = []
    for index in range(len(data[column])):
        if is_nan(data[column][index]):
            result.append(index)
    return result
# Determine the rows will be deleted
def delete_row(data, limit_number) -> None:
    if not (1 <= limit_number <= len(data.keys())):
        raise ValueError('Invalid number of missing values')
    # Determine the indexes of missing rows in each column
    index_rows = []
    for feature in data.keys():
        index_rows += index_empty_row(data, feature)
    # Count the missing values in each row
    index_dict = {}
    for index in index_rows:
        if index not in index_dict.keys():
            index_dict[index] = 1
        else:
            index_dict[index] += 1
    # Sort this dictionary descending by keys, because the next step we will remove some row
    # And if we remove the rows at the end first, the indexes of the rest will not be affected
    sorted_index_dict = sorted(index_dict.items(), key= lambda x: x[0], reverse=True)
    # convert it back to dictionary
    index_dict = {item[0]: item[1] for item in sorted_index_dict}
    # Determine the row will be deleted
    for index in index_dict.keys():
        if index_dict[index] >= limit_number:
            for feature in data.keys():
                data[feature].pop(index)
                
def main():
    data = read_file('house-prices.csv')
    delete_row(data, 15)
    create_csv_file('result.csv', data)
    
if __name__ == '__main__':
    main()
    