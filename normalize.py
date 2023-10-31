from main import *

# calculate the mean of a feature
def mean_feature(feature): 
    s = sum([value for value in feature if not is_nan(value)])
    l = len([value for value in feature if not is_nan(value)])
    return s/l
# calculate the standard deviation of a feature
def std_feature(feature):
    mean = mean_feature(feature)
    total_deviation = sum([(value - mean)** 2 for value in feature if not is_nan(value)])
    l = len([value for value in feature if not is_nan(value)])
    return (total_deviation/l)**0.5 
# Apply z-score method
def zscore_method(feature):
    mean = mean_feature(feature)
    std = std_feature(feature)
    return [(value - mean)/std if not is_nan(value) else value for value in feature]
# Apply min-max method
def min_max_method(feature):
    for value in feature:
        if not is_nan(value):
            min = max = value
            break
        
    for value in feature:
        if not is_nan(value):
            if value < min:
                min = value
            if value > max:
                max = value
    return [(value - min)/(max - min) if not is_nan(value) else value 
            for value in feature]
# Find the numerical features
def num_feature(data):
    num_feature = [feature for feature in data.keys()]
    for feature in data.keys():
        for value in data[feature]:
            if type(value) == str:
                num_feature.remove(feature)
                break
    return num_feature
# Normalize the data
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
    # get all the arguments from the command line
    arguments = parse_cmd()
    # parsing the arguments
    filename = arguments[0].split('=')[1]
    method = arguments[1].split('=')[1]
    column = arguments[2].split('=')[1]
    filename_out = arguments[3].split('=')[1]
    # Load the data from the file
    data = read_file(filename)
    # normalize the data and save the result to the output file
    normalize(data, column, method)
    create_csv_file(filename_out, data)
    
if __name__ == '__main__':
    main()