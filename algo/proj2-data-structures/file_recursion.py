import os
import sys
from collections import deque


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
    files = []
    q = deque([path])
    while len(q):
        current_dir = q.pop()
        for obj in os.listdir(current_dir):
            obj_path = os.path.join(current_dir, obj)
            if os.path.isfile(obj_path) and obj_path.endswith(suffix):
                files.append(obj_path)
            if os.path.isdir(obj_path):
                q.appendleft(obj_path)
    return sorted(files)


if __name__ == "__main__":
    input_suffix, input_path = "", ""
    try:
        input_suffix = sys.argv[1]
        input_path = sys.argv[2]
    except IndexError:
        sys.exit(
            "Initial directory and file suffix required. E.g. 'file_recursion.py cpp testdir'")
    files = find_files(input_suffix, input_path)
    for f in files:
        print(f)
