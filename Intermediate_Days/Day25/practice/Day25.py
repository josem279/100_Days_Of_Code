############### Reading from CSV files
from pprint import pprint
import csv
import pandas as pd


# Traditional way of reading CSV:
# with open('Intermediate_Days\Day25\practice\weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(data)
# print(temperatures)

############### Using pandas

### Pandas for CSVs
data = pd.read_csv('Intermediate_Days\Day25\practice\weather_data.csv')
# print(file)

### Pandas can tell the name of cols:
# print(data['temp'])

### Other uses for Pandas:

# Identifying types Dfs and Series
# print(type(data))
# print(type(data['temp']))

data_dict = data.to_dict()
# pprint(data_dict)

temp_list = data['temp'].to_list()
# print(temp_list)

# EDA with pandas
# print(f"Average temp is: {data['temp'].mean()}")
# print(f"Max temp is: {data['temp'].max()}")

### Getting data into columns:
# print(data['condition'])
# print(data.condition)

### Working with DataFrames
monday_data = data[data['day'] == "Monday"] 
# print(monday_data) # Row for Monday
max_temp_data = data[data['temp'] == data['temp'].max()] 
# print(max_temp_data) # Row for day with max temp
monday_temp_f = monday_data['temp'] * 9/5 + 32 
# print(f"Monday temp in F: {monday_temp_f}")

### Creating a DF from scratch:
data_dict = {
    "students": ["Jose", "Luis"],
    "Scores": [70, 80]
}

data = pd.DataFrame(data_dict)
print(data)