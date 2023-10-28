from main import *

def remove_duplicate(data):
    rows = []
    index_deleted_rows = []
    # Determine the index of duplicate row
    first_column = list(data.keys())[0]
    for i in range(len(data[first_column])):
        row = []
        for feature in data.keys():
            row.append(data[feature][i])
        if row not in rows:
            rows.append(row)
        else:
            index_deleted_rows.append(i)
    # Reverse the index list for removable purpose
    index_deleted_rows.reverse()
    # Remove the duplicate rows
    for index in index_deleted_rows:
        for feature in data.keys():
            data[feature].pop(index)

def main():
    data = read_file('house-prices.csv')      
    remove_duplicate(data)
    
if __name__ == '__main__':
    main()
