"""
Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it)
that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

    ./testdir
    ./testdir/subdir1
    ./testdir/subdir1/a.c
    ./testdir/subdir1/a.h
    ./testdir/subdir2
    ./testdir/subdir2/.gitkeep
    ./testdir/subdir3
    ./testdir/subdir3/subsubdir1
    ./testdir/subdir3/subsubdir1/b.c
    ./testdir/subdir3/subsubdir1/b.h
    ./testdir/subdir4
    ./testdir/subdir4/.gitkeep
    ./testdir/subdir5
    ./testdir/subdir5/a.c
    ./testdir/subdir5/a.h
    ./testdir/t1.c
    ./testdir/t1.h


Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not
allowed to use os.walk().

Here is some code for the function to get you started:

"""

import os



def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # If the first directory does not exist return empty list.
    if not (os.path.isdir(path) or os.path.isfile(path)) :
        return []

    # If suffix is an empty string returns en empty list
    if suffix == "":
        return []


    if os.path.isfile(path):
        return [path] if path.endswith(suffix) else []

    path_list = []
    for entry_name in os.listdir(path):
        path_list += find_files(suffix, os.path.join(path, entry_name))

    return path_list


# Test cases

print(find_files(".c", "./testdir"))
# prints ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files(".gitkeep", "./testdir"))
# prints ['./testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep']

print(find_files(".jpg", "./testdir"))
# prints [] because the suffix ".jpg" is not present in "./testdir" path.

print(find_files("", "./testdir"))
# prints [] suffix is an empty string.

print(find_files(".jpg", "not_exist_directory"))
# prints [] the directory does not exist.