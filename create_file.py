import os
import time


def make_directory():
    timestr = time.strftime("%d.%m.%Y %H:%M:%S")

    # Directory
    directory = timestr

    # Parent Directory path
    parent_dir = "/Users/natalka/PycharmProjects/cutvideo"

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    try:
        os.mkdir(path)
    except OSError:
        pass
    print("Directory '% s' created" % directory)

make_directory()