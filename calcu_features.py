from main import *


def num_feature(data):
    num_feature = [feature for feature in data.keys()]
    for feature in data.keys():
        for value in data[feature]:
            if type(value) == str:
                num_feature.remove(feature)
                break
    return num_feature

def calculate_num_feature(data, feature1, feature2, operation):
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
    arguments = parse_cmd()
    filename = arguments[0].split('=')[1]
    method = arguments[1].split('=')[1]
    feature1 = arguments[2].split('=')[1]
    feature2 = arguments[3].split('=')[1]
    filename_out = arguments[4].split('=')[1]
    data = read_file(filename)
    result = calculate_num_feature(data, feature1, feature2, method)
    new_data = {result[0]: 
                result[1]}
    create_csv_file(filename_out, new_data)
    
if __name__ == '__main__':
    main()
    
