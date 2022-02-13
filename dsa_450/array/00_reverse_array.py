"""
Write a program to reverse an array or string
Given an array (or string), the task is to reverse the array/string.

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
Caveats:
    1. Don't assume dynamic lists
    2. Don't assume we know the list/array size early
"""
from typing import List


def reverse_array(input: List) -> List:
    """
    Caveats:
    1. Don't assume dynamic lists
    2. Don't assume we know the list/array size early
    Approach1:
    1. count the number of elements
    2. Start a new array of same length
    3. access them in reverse order
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    inp_len = len(input)
    output = []
    for i in range(inp_len):
        element = input[inp_len - i - 1]
        output.append(element)
    return output


def reverse_array2(input: List) -> List:
    """
    Approach2: Sliding Window in place
    1. count the number of elements
    2. Swap elements in place
    Time Complexity: O(n)
    Space Complexity: 0/ no extra memory required
    """
    inp_len = len(input)
    l_pointer, r_pointer = 0, inp_len - 1
    while l_pointer < r_pointer:
        input[l_pointer], input[r_pointer] = input[r_pointer], input[l_pointer]
        l_pointer += 1
        r_pointer -= 1
    return input


def reverse_array3(input: List) -> List:
    """
    Approach3: TODO: Recursive
    1. count the number of elements
    2. Recursively apply Swap elements in place
    Time Complexity: O(n)
    Space Complexity: 0/ no extra memory required
    """
    return input


def test_reverse_array(func):
    assert func([]) == []
    assert func([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert func(["a", "b", "c", "d"]) == ["d", "c", "b", "a"]
    assert func(["a", "b", 4, 3]) == [3, 4, "b", "a"]
    # assert reverse_array({"a": 1, "b": 1, 4: 1, 3: 1}) == {3: 1, 4: 1, "b": 1, "a": 1}


print("before __name__ guard")
if __name__ == "__main__":
    test_reverse_array(reverse_array)
    print("test cases succesful1")
    test_reverse_array(reverse_array2)
    print("test cases succesful2")
print("after __name__ guard")
