import os


def find(path, dir):
    for root, dirs, files in os.walk(path):
        if dir in dirs:
            print(os.path.abspath(os.path.join(root, dir)))
