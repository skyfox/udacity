def sqrt(num: int) -> int:
    """Calculates a floor value of a square root of a given number.

    Binary-tree based search.

    Args:
          num: input number

    Returns:
          square root of a given number, rounded.
    """
    if num < 0:
        raise ValueError("Can't calculate square root of number without imaginary part.")
    if num == 0:
        return 0

    left, right = 0, num
    while left != right:
        middle = (right + left) // 2
        middle_sqr = middle * middle

        # If the algorithm converges to an interval [value, value + 1] and the remainder of the division not equal 0
        # left or right interval bound is the answer. One of them is closer. Check and return the closest.
        if right - left == 1:
            return left if abs(num - left * left) <= abs(num - right * right) else right

        if middle_sqr > num:
            right = middle
        elif middle_sqr < num:
            left = middle
        else:
            return middle


if __name__ == "__main__":
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
