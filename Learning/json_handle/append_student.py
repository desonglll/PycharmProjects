import json
from . import is_json_empty


def append_student(file_path):
    with open(file_path, "r") as file:
        if is_json_empty.is_json_empty(file_path):
            data = []
        else:
            data = json.load(file)

    while True:
        name = str(input("name:"))
        if name == "-1":
            break
        gender = str(input("gender:"))
        age = int(input("age:"))
        index = int(input("index:"))

        student = {
            "name": name,
            "gender": gender,
            "age": age,
            "index": index
        }
        data.append(student)
    with open(file_path, "w") as file:
        json.dump(data, file)
