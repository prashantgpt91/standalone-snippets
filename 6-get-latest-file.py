import os
import glob

"""Returns the name of the latest (most recent) file
of the joined path(s)"""

def get_latest_file(path, *paths):
    fullpath = os.path.join(path, *paths)
    list_of_files = glob.glob(fullpath)  # use iglob in Python3
    if not list_of_files:
        return None
    latest_file = max(list_of_files, key=os.path.getctime)
    _, filename = os.path.split(latest_file)
    return filename


if __name__ == "__main__":
    p = get_latest_file('1', '*')
    print p

