import json


def write_to_file(file_name, list_name):
    with open(file_name, "w") as file:
        for element in list_name:
            file.write(element + "\n")


def read_file(file_name):
    with open(file_name) as file:
        content = file.readlines()
    return content


def dict_to_json(file_name, dict_name):
    with open(file_name, "w") as file:
        json.dump(dict_name, file, indent=4)


def json_to_dict(file_name):
    with open(file_name) as file:
        content = file.read()
    return content

