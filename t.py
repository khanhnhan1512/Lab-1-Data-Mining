# Sample dictionary-oriented list
data = {
    'name': ['John', 'Alice', 'John', 'Bob', 'Alice'],
    'age': [25, 30, 5, 30, 35]
}

# Initialize an empty set to track unique rows
unique_rows = set()

# Initialize an empty dictionary to store unique rows
unique_data = {}

# Iterate over the rows in the dictionary-oriented list
for i in range(len(data['name'])):
    row = tuple(data[column][i] for column in data.keys())
    # Check if the row is already in the set of unique rows
    if row not in unique_rows:
        unique_rows.add(row)
        # Add the row to the unique_data dictionary
        for column in data.keys():
            unique_data.setdefault(column, []).append(data[column][i])

# Print the modified dictionary-oriented list without duplicate rows
for column, values in unique_data.items():
    print(f"{column}: {values}")