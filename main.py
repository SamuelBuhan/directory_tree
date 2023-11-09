import os
import shutil


def file_list(path):
    print(f"Here is the file in the directory {path}--->")
    files = os.listdir(path)
    for file in files:
        print(file)
    return files


def main():
    pwd = os.getcwd()
    file_list(pwd)



if __name__ == "__main__":
    main()
