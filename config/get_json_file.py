import json

def get_json_file(json_file):
    with open(json_file,encoding= "utf-8") as file:
        return json.load(file)