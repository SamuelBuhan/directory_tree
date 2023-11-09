import os
import shutil


def file_list(path):
    print(f"Here is the file in the directory {path}--->")
    files = os.listdir(path)
    for file in files:
        print(file)
    return files

def file_exist(path, filename):
    files = file_list(path)
    for file in files:
        if file == filename:
            return True
    return False

def create_file(path, filename, text):
    exist = file_exist(path, filename)
    if not(exist):
        file_path = f"{path}/{filename}"
        file = open(file_path, "w")
        file.write(text)
        file.close()
    return True

def main():
    pwd = os.getcwd()
    file_list(pwd)
    exist = file_exist(pwd, "hello.py")
    print(f"is hello.py already exists:{exist}")
    file_exist(pwd, "main.py")
    print(f"is main.py already exists:{exist}")
    text = "hello, this is the first line for my text"
    create_file(pwd, "test.txt", text)
    file_list(pwd)


if __name__ == "__main__":
    main()
