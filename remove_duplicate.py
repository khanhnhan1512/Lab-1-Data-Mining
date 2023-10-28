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
    print(f'Removed {len(index_deleted_rows)} duplicate row(s).')

def main():
    arguments = parse_cmd()
    filename = arguments[0].split('=')[1]  
    filename_out = arguments[1].split('=')[1]
    data = read_file(filename)      
    remove_duplicate(data)
    create_csv_file(filename_out, data)
    
if __name__ == '__main__':
    main()
