def write_file(file_name, file_content):
    path = f"{file_name}.txt"
    with open(path, mode="w", encoding="utf-8") as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
    path = f"{file_name}.txt"
    with open(path, mode="a") as text_file:
        text_file.write(append_content)
    pass

def read_file(file_name):
    path = f"{file_name}.txt"
    with open(path, mode="r", encoding="utf-8") as text_file:
        return text_file.read()

