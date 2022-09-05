with open('weather_data.csv', mode='r') as data_source:
    data = data_source.read().split('\n')
    for data_point in data:
        print(data_point)