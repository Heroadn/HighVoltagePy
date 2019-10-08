import json
def fileToJson(file):
    with open(file) as json_data:
        return json.load(json_data)