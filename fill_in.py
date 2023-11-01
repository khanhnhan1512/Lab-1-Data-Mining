from main import *
from extract_column import *

# Classify the numerical and categorical features
def classify_features(data) -> list:
    missing_feature = extract_column(data)
    cat_feature = []
    for feature in missing_feature:
        for value in data[feature]:
            if type(value) == str:
                cat_feature.append(feature)
                break
    num_feature = [feature for feature in missing_feature if feature not in cat_feature]
    return num_feature, cat_feature
# Find the rows with missing values for specific column
def index_empty_row(data, column) -> list:
    result = []
    for index in range(len(data[column])):
        if is_nan(data[column][index]):
            result.append(index)
    return result
# Fill in the missing values
def fill_in(data, method, column) -> None:
  num_attr, cate_attr = classify_features(data)
  empty_row = index_empty_row(data, column)
  if method == 'mean':
    if column not in num_attr:
      raise ValueError('Column must be numerical or not have missing value')
    else:
      for index in empty_row:
        data[column][index] = 0
      missing_value = sum(data[column]) / (len(data[column])-len(empty_row)) 
  elif method == 'median':
      if column not in num_attr:
        raise ValueError('Column must be numerical or not have missing value')
      else:
        not_empty_row = [data[column][i] for i in range(len(data[column])) if i not in empty_row]
        not_empty_row.sort()
        number_not_empty_row = len(not_empty_row)
        if number_not_empty_row % 2 == 0:
          missing_value = (not_empty_row[number_not_empty_row/2] + not_empty_row[number_not_empty_row/2 - 1])/2
        else:
          missing_value = not_empty_row[number_not_empty_row//2]
  elif method == 'mod':
    if column not in cate_attr:
      raise ValueError('Column must be categorical or not have missing value')
    else:
      value_dict = {}
      for index in range(len(data[column])):
        if index not in empty_row:
          if data[column][index] not in value_dict.keys():
            value_dict[data[column][index]] = 1
          else:
            value_dict[data[column][index]] += 1
      value_dict = sorted(value_dict.items(), key= lambda x: x[1], reverse=True)
      missing_value = value_dict[0][0]
  else:
      raise ValueError('Method must be mean, median, or mode')
  # Fill missing value
  print(f'The missing value is {missing_value}')
  for index in empty_row:
    data[column][index] = missing_value
    
def main():
    # get all the arguments from command line
    arguments = parse_cmd()
    # parsing to get the arguments
    filename = arguments[0].split('=')[1]
    method = arguments[1].split('=')[1]
    column = arguments[2].split('=')[1]
    filename_out = arguments[3].split('=')[1]
    # Load the data from the file
    data = read_file(filename)
    # Fill in the missing values and save the new data to the output file
    fill_in(data, method, column)
    create_csv_file(filename_out, data)
    
if __name__ == '__main__':
    main()