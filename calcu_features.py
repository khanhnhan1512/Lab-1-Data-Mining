from main import *

# return a list contains all the numerical features
def num_feature(data) -> list:
    num_feature = [feature for feature in data.keys()]
    for feature in data.keys():
        for value in data[feature]:
            if type(value) == str:
                num_feature.remove(feature)
                break
    return num_feature
# Perform the operation on the two features and return a tuple of the operation and the result
def calculate_num_feature(data, feature1, feature2, operation) -> tuple:
    num_attr = num_feature(data)
    if feature1 not in num_attr or feature2 not in num_attr:
        raise ValueError('Feature must be numerical')
    if operation not in ['add', 'sub', 'mul', 'div']:
        raise ValueError('Operation must be add, sub, mul or div')
    if operation == 'add':
        return 'Add', [value1 + value2 for value1, value2 in zip(data[feature1], data[feature2])]
    elif operation == 'sub':
        return 'Sub', [value1 - value2 for value1, value2 in zip(data[feature1], data[feature2])]
    elif operation == 'mul':   
        return 'Mul', [value1 * value2 for value1, value2 in zip(data[feature1], data[feature2])]
    elif operation == 'div':
        return 'Div', [value1 / value2 for value1, value2 in zip(data[feature1], data[feature2])]

def main():
    # get all the arguments from the command line
    arguments = parse_cmd()
    # parsing the arguments
    filename = arguments[0].split('=')[1]
    method = arguments[1].split('=')[1]
    feature1 = arguments[2].split('=')[1]
    feature2 = arguments[3].split('=')[1]
    filename_out = arguments[4].split('=')[1]
    # Load the data from the file
    data = read_file(filename)
    # Calculate the result
    result = calculate_num_feature(data, feature1, feature2, method)
    new_data = {result[0]: 
                result[1]}
    # Write the result to the file
    create_csv_file(filename_out, new_data)
    
if __name__ == '__main__':
    main()
    
