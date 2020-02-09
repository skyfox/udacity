from typing import List


def find_pivot(arr: List[int]) -> int:
    """Finds rotation pivot.

    Args:
        arr: rotated array.

    Returns:
        index if a pivot element.
    """
    left, right = 0, len(arr) - 1
    while left != right:
        middle = (right + left) // 2
        if arr[middle] > arr[right]:
            left = middle + 1
        else:
            right = middle
    return left


def rotated_array_search(arr: List[int], key: int) -> int:
    """Finds the index of a key in a rotated array.

    Args:
        arr: rotated array.
        key: the key to find.

    Returns:
        the index in the array or -1 of not found.
    """
    pivot = find_pivot(arr)
    left, right = pivot, (pivot + len(arr) - 1) % len(arr)
    while left != right:
        middle = ((((right - pivot) % len(arr) + (left - pivot) % len(arr)) // 2) + pivot) % len(arr)
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            right = middle
        else:
            left = (middle + 1) % len(arr)
    # The loop finishes once left and right point to the same element.
    # But the element itself can also be the answer. Check before return.
    return left if arr[left] == key else -1


if __name__ == "__main__":
    pass
