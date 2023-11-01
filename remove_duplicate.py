from main import *


# Remove the duplicate rows
def remove_duplicate(data) -> None:
    # Use a dictionary to store the unique rows
    unquie_rows = {}
    # Use a list to store the index of the duplicate rows
    deleted_index = []
    total_row = len(data[list(data.keys())[0]])
    for i in range(total_row):
        row = []
        for col in data.keys():
            row.append(data[col][i])
        # because set can't store list (unhashable), so convert the list to string  
        if str(row) not in unquie_rows:
            unquie_rows[str(row)] = 1
        else:
            deleted_index.append(i)
    # delete the duplicate rows
    for col in data.keys():
        data[col] = [data[col][i] for i in range(len(data[col])) if i not in deleted_index]
    print(f'The number of duplicate row: {len(deleted_index)}')

def main():
    # get all the arguments from the command line
    arguments = parse_cmd()
    # parsing the arguments
    filename = arguments[0].split('=')[1]  
    filename_out = arguments[1].split('=')[1]
    # Load the data from the file
    data = read_file(filename)   
    # remove the duplicate rows and save the result to the output file   
    remove_duplicate(data)
    create_csv_file(filename_out, data)
    
if __name__ == '__main__':
    main()
