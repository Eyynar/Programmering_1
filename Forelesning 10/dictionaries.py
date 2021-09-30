persons = {
    "person1": {
        "name": "Einar",
        "birthday": "19.01.2001"
    },

    "person2": {
        "name": "Georg",
        "birthday": "14.06.2003"
    },

}

# print(persons.get("person1").get("name"))

for key in persons:
    for key2 in persons[key]:
        print(persons[key][key2])


for key, value in persons.items():
    for val in value.values():
        print(val)
