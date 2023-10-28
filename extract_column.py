from main import *

# Find the columns with missing values
def extract_column(data) -> list:
    result = []
    for feature in data.keys():
        for value in data[feature]:
            if is_nan(value):
                result.append(feature)
                break
    return result

def main():
    # get all the arguments from the command line
    argments = parse_cmd()
    # parsing the arguments
    filename = argments[0].split('=')[1]
    # Load the data from the file
    data = read_file(filename)
    # get the result and print it
    columns = extract_column(data)
    print(f'There are {len(columns)} columns with missing values: ')
    for column in columns:
        print(column)
    
if __name__ == '__main__':
    main()