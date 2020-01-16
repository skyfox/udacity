import os
import sys
from collections import deque
from typing import Text, List


def find_files(suffix: Text, path: Text) -> List[Text]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix: suffix if the file name to be found
      path: path of the file system

    Returns:
       a list of paths
    """
    # The case when a file instead of a directory was provided as a path.
    if os.path.isfile(path):
        return [path] if path.endswith(suffix) else []

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
    return files


if __name__ == "__main__":
    input_suffix, input_path = "", ""
    try:
        input_suffix = sys.argv[1]
        input_path = sys.argv[2]
    except IndexError:
        sys.exit(
            "Initial directory and file suffix required. E.g. 'file_recursion.py cpp testdir'")
    found = find_files(input_suffix, input_path)
    for f in found:
        print(f)
