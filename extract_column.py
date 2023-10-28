from main import *


def extract_column(data) -> list:
    result = []
    for feature in data.keys():
        for value in data[feature]:
            if is_nan(value):
                result.append(feature)
                break
    return result

def main():
    argments = parse_cmd()
    filename = argments[0].split('=')[1]
    data = read_file(filename)
    columns = extract_column(data)
    print(f'There are {len(columns)} columns with missing values: ')
    for column in columns:
        print(column)
    
if __name__ == '__main__':
    main()