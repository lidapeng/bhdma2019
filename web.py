# web operations

# file operations
import os


def getCurrentPath():
    cwd = os.getcwd()
    return cwd


if __name__ == "__main__":
    # execute only if run as a script

    print(getCurrentPath())

