import file_handler

list_dyr = ["Katt", "Hund", "Fugl"]

dict_dyr = {
    "species": "Katt",
    "age": 9
}

file_handler.write_to_file("dyr.txt", list_dyr)
print(file_handler.read_file("dyr.txt"))

file_handler.dict_to_json("dyr.json", dict_dyr)
print(file_handler.json_to_dict("dyr.json"))
