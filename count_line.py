from main import *

# return the number of lines with missing values
def count_line_with_missing_values(data) -> int:
    index_empty_row = set()
    for feature in data.keys():
        for index,value in enumerate(data[feature]):
            if is_nan(value):
                index_empty_row.add(index)
    return len(index_empty_row)

def main():
    # get all the arguments from the command line
    arguments = parse_cmd()
    # parsing the arguments
    filename = arguments[0].split('=')[1]
    # Load the data from the file
    data = read_file(filename)
    # Calculate the result and print it
    print(f"There are total {count_line_with_missing_values(data)} lines with missing values")
    
if __name__ == '__main__':
    main()