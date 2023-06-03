import json


def handle_json():
    with open("students.json", "r") as file:
        data = json.load(file)

    for student in data:
        name = student["name"]
        gender = student["gender"]
        age = student["age"]
        print(f"name:{name}, gender:{gender}, age:{age}")
