# Importing the json library.
import json

# Creating a Json Object.

data = {
  'name': 'John Doe',
  'aga': 30,
  'city': 'New York, NY',
  'interests':['Traveling', 'Football', 'Golf', 'Running', 'VideoGames', 'History'],
  'is_student': False
}


# Creating a Json object and writing the python object contents to the json.
with open('data.json', 'w') as json_file:

  json.dump(data, json_file, indent=4)

print("Data has been written to data.json")

# Reading the Json object and printing the output to the terminal.
with open('data.json','r') as json_file:

  # Creating a variable to hold the json file contents
  loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

# Adding to the JSON Object.
loaded_data['age'] = 34
loaded_data['interests'].append('Secret Hobby')

# Write the changes to the json file.
with open('data.json', 'w') as json_file:

  json.dump(loaded_data, json_file, indent=4)

print("Data has been written to data.json")