import os

def start() -> str:
    file_path = input("Please enter the path to the file: ")
    if os.path.exists(file_path):
        return file_path
    else:
        return ('File not found')

if __name__ == '__main__':
    print(start())
