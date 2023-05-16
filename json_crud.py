import json

def json_edit(file_name, mode, json_metod, indent=None, **dict_):
    with open(file_name, mode) as file:
        json_metod(dict_,file, indent=indent)

#creats a brand new json file
def create_new_json(file_name='linkedin_stuffs.json',indent=2,**dict_):
    #write json file
    json_edit(file_name, 'w', json.dump, indent, **dict_)

#yep, it reads...
def read_json(file_name = 'linkedin_stuffs.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

#appends new values to json file
def update_json(file_name = 'linkedin_stuffs.json',indent=2, **dict_):

    # Load existing JSON data from file
    data = read_json(file_name)
    # Add a new value to the dictionary
    data.update(dict_)
    # Write the updated JSON data back to the file
    create_new_json(file_name, indent,**data)
    print(f'{file_name} updated')

def delete_key(key_to_remove,file_name = 'linkedin_stuffs.json'):

    # Load the JSON data from the file into a Python object
    data = read_json(file_name)
    # Remove a key-value pair from the Python object
    if key_to_remove in data:
        data.pop(key_to_remove)
    # Write the modified Python object back to the file
        create_new_json(file_name, indent=2, **data)
    else: print('key not found')
