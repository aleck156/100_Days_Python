import csv
import pandas

with open('weather_data.csv', mode='r') as data_source:
    data = data_source.read().split('\n')
    for data_point in data:
        print(data_point)

with open('weather_data.csv') as data_source:
    output = csv.reader(data_source)
    temperatures = []
    for index, row in enumerate(output):
        if index == 0:
            continue
        temperatures.append(int(row[1]))
    print(temperatures)

data = pandas.read_csv('weather_data.csv')
print(data)
data_dict = data.to_dict()
temp_list = data['temp'].tolist()
# print(f'{sum(temp_list)/len(temp_list):.2f} \u00b0C')

max_value = data['temp'].max()
# print(f'Max value: {max_value:.2f} \u00b0C')

# print(data[data.temp == data['temp'].max()])

print(f'TEMP: {int(data[data.day == "Monday"].temp) * 1.8 + 32} \u00b0C')

data_dict = {
    'students': ['Anne', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv('new_data.csv')
print(data_frame)