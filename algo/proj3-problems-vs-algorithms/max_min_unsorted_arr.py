import random
from typing import List, Tuple


def get_min_max(arr: List[int]) -> Tuple[float, float]:
    """
    Returns a tuple(min, max) out of list of unsorted integers.

    Returns (+inf, -inf) if input array is empty.

    Args:
       arr: list of integers containing one or more integers.

    Returns:
        a tuple of 2 elements: (min, max).
    """
    min_num, max_num = float("inf"), float("-inf")
    for num in arr:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num


if __name__ == "__main__":
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")