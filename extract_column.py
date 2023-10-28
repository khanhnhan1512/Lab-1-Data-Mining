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
    data = read_file('house-prices.csv')
    print(extract_column(data))
    
if __name__ == '__main__':
    main()