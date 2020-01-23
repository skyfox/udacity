from collections import Counter
from typing import List


def sort_012(arr: List[int]) -> List[int]:
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       arr: list to be sorted

    Returns:
        sorted list
    """
    counter = Counter(arr)
    sorted_arr = []
    for i in [0, 1, 2]:
        sorted_arr.extend([i] * counter[i])
    return sorted_arr


if __name__ == "__main__":
    arr = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    assert sorted(arr) == sort_012(arr)
