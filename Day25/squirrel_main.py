import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

new_data = data["Primary Fur Color"].dropna().unique().tolist()
squirrel_count = {
    'Fur Color': [],
    'Count': []
}
for key in new_data:
    squirrel_count['Fur Color'].append(key)
    squirrel_count['Count'].append(len(data[data['Primary Fur Color'] == key]))
results = pandas.DataFrame(squirrel_count)
print(results)
results.to_csv('squirrel_count.csv')