import json

from . import is_json_empty


def show_students(file_path):
    if is_json_empty.is_json_empty(file_path):
        print("JSON 文件为空")
    else:
        with open(file_path, "r") as file:
            data = json.load(file)
            for student in data:
                index = student["index"]
                name = student["name"]
                gender = student["gender"]
                age = student["age"]
                print(f"index:{index}, name:{name}, gender:{gender}, age:{age}")
