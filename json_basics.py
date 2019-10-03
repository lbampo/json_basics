import json

car_data = {
    'engine': 'electric',
    'brand': 'Peugeot',
    'price': '13,000',
    'model' : 'Ze'
}

print(type(car_data))

car_data_json_string = json.dumps(car_data)

print(car_data_json_string)
print(type(car_data_json_string))

car_data = {'engine': 'electric', 'brand': 'Peugeot', 'price': '13,000', 'model' : 'Ze'}

with open('new_json_file.json' , 'w') as jsonfile:
    json.dump(car_data, jsonfile)
    # json.dump(arg1, arg2) --> .json file
        #arg1 is a dictionary
        #arg2 is the file to dump the json
