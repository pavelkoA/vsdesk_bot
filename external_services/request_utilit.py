import json

def we_read_user_data_json(data_path="..\\data\\user_data.json"):
    with open(data_path, 'r', encoding='utf-8') as data_file:
        data_file_dict = json.load(data_file)
    return data_file_dict
