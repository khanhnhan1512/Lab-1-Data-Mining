from main import *


def mean_feature(feature): 
    s = sum([value for value in feature if not is_nan(value)])
    l = len([value for value in feature if not is_nan(value)])
    return s/l

def std_feature(feature):
    mean = mean_feature(feature)
    total_deviation = sum([(value - mean)** 2 for value in feature if not is_nan(value)])
    l = len([value for value in feature if not is_nan(value)])
    return (total_deviation/l)**0.5 

def zscore_method(feature):
    mean = mean_feature(feature)
    std = std_feature(feature)
    return [(value - mean)/std if not is_nan(value) else value for value in feature]

def min_max_method(feature):
    return [(value - min(feature))/(max(feature) - min(feature)) if not is_nan(value) else value 
            for value in feature]

def num_feature(data):
    num_feature = [feature for feature in data.keys()]
    for feature in data.keys():
        for value in data[feature]:
            if type(value) == str:
                num_feature.remove(feature)
                break
    return num_feature

def normalize(data, column, method):
    num_attr = num_feature(data)
    if column not in num_attr:
        raise ValueError('Column must be numerical')
    if method == 'min-max':
        data[column] = min_max_method(data[column])
    elif method == 'z-score':
        data[column] = zscore_method(data[column])
    else:
        raise ValueError('Method must be min-max or z-score')
    
def main():
    arguments = parse_cmd()
    filename = arguments[0].split('=')[1]
    method = arguments[1].split('=')[1]
    column = arguments[2].split('=')[1]
    filename_out = arguments[3].split('=')[1]
    data = read_file(filename)
    normalize(data, column, method)
    create_csv_file(filename_out, data)
    
if __name__ == '__main__':
    main()