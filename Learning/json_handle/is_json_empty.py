
def is_json_empty(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
        if not file_content:
            return True
    return False


