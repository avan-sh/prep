"""
Maximum and minimum of an array using minimum number of comparisons
Write a C function to return minimum and maximum in an array. 
Your program should make the minimum number of comparisons. 
Q1: What if empty Array? return None
Q2: Can I assume all numeric inputs? Yes
Q3: 
"""

from typing import List, Tuple


def update_min_max(val, min, max):
    min = val if val < min else min
    max = val if val > max else max
    return min, max


def min_max_array1(input: List) -> Tuple[int]:
    """
    Approach1:
    1. Initiate Min & Max values as None
    2. Iterate through array to continously update min and max values
    Note: Comparision btwn None and numeric is not possible.
    so to decrease comparisions needed, set min max values as 1st element to start
    time_complexity: O(n)
    Space_comp: O(1) no elements increasing with increasing time.
    Num comparisions: 2n For each element, compare with existing min, max
    """
    arr_len = len(input)
    if arr_len == 0:
        return None, None
    min, max = input[0], input[0]
    for i in input:
        min, max = update_min_max(i, min, max)
    return min, max


def min_max_array2(input: List) -> Tuple[int]:
    """
    Approach2:
    Recursive approach
    Break into two and calculate min, max values recursively
    Num Comparisions:
    TODO: Implement above & calculate
    TODO: Recap on Divide and conquer
    """
    arr_len = len(input)
    if arr_len == 0:
        return None, None
    min, max = input[0], input[0]
    for i in input:
        min, max = update_min_max(i, min, max)
    return min, max


def test_update_min_max():
    assert update_min_max(0, 1, 4) == (0, 4)
    assert update_min_max(-10, 1, 4) == (-10, 4)
    assert update_min_max(10, 1, 4) == (1, 10)
    assert update_min_max(-10, -100, 4) == (-100, 4)
    pass


def test_min_max_array(func):
    assert func([]) == (None, None)
    assert func([1, 1, 1, 1]) == (1, 1)
    assert func([1, 2, 3, 4]) == (1, 4)
    assert func([-1, -2, -3, -4]) == (-4, -1)
    pass


if __name__ == "__main__":
    test_update_min_max()
    test_min_max_array(min_max_array1)
