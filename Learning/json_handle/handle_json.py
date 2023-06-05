import json


def handle_json():
    with open("../data/students.json", "r") as file:
        data = json.load(file)

    for student in data:
        name = student["name"]
        gender = student["gender"]
        age = student["age"]
        index = student["index"]
        print(f"index:{index}, name:{name}, gender:{gender}, age:{age}")
