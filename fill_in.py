from main import *
from extract_column import *

# Extract the numerical and categorical features
def categorizing_feature(data) -> list:
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
  num_attr, cate_attr = categorizing_feature(data)
  empty_row = index_empty_row(data, column)
  if method == 'mean':
    if column not in num_attr:
      raise ValueError('Column must be numerical')
    else:
      for index in empty_row:
        data[column][index] = 0
      missing_value = sum(data[column]) / len(data[column])    
  elif method == 'median':
      if column not in num_attr:
        raise ValueError('Column must be numerical')
      else:
        not_empty_row = [data[column][i] for i in range(len(data[column])) if i not in empty_row]
        number_not_empty_row = len(not_empty_row)
        if number_not_empty_row % 2 == 0:
          missing_value = (not_empty_row[number_not_empty_row/2] + not_empty_row[number_not_empty_row/2 - 1])/2
        else:
          missing_value = not_empty_row[number_not_empty_row//2]
  elif method == 'mod':
    if column not in cate_attr:
      raise ValueError('Column must be categorical')
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
  for index in empty_row:
    data[column][index] = missing_value
    
def main():
    data = read_file('house-prices.csv')
    fill_in(data, 'mod', 'Alley')
    create_csv_file('result.csv', data)
    
if __name__ == '__main__':
    main()