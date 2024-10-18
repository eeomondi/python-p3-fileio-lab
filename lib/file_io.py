def write_file(file_name, content):
    with open(f"{file_name}.txt", 'w') as f:
        f.write(content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", 'a') as f:  # Use 'a' mode to append
        f.write(append_content)


def read_file(file_name):
    with open(f"{file_name}.txt", 'r') as f:
        return f.read()
