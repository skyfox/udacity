from typing import List
from collections import deque


def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    """Merges 2 pre-sorted lists into one.

    Args:
        arr1: first pre-sorted array.
        arr2: second pre-sorted array.

    Returns:
        merged sorted array.
    """
    merged_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    merged_arr.extend(arr1[i:]) if i < len(arr1) else merged_arr.extend(arr2[j:])
    return merged_arr


def rearrange_digits(arr: List[int]) -> List[int]:
    """Form a list of 2 number such that their sum is maximum.

    Args:
        arr: input list if numbers.

    Returns:
        a list of 2 numbers such that their sum is maximum.
    """
    if len(arr) < 2:
        raise ValueError("Input list can has to have 2 elements or more.")
    # MergeSort the input list.
    q = deque()
    for digit in arr:
        q.append([digit])
    while len(q) > 1:
        q.appendleft(merge(q.pop(), q.pop()))
    # Combine 2 final numbers
    num1, num2 = "", ""
    for i, digit in enumerate(q.pop()[::-1]):
        if i % 2 == 0:
            num1 += str(digit)
        else:
            num2 += str(digit)
    return [int(num1), int(num2)]


if __name__ == "__main__":
    print(rearrange_digits([1, 2, 3, 4, 5]))
