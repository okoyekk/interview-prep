from typing import List

def solution(A: List[int]):
    # edge case - single element array
    if len(A) == 1:
        return A[0]
    # base case - check if all elements are zero
    if is_zero(A):
        return 0
    strokes = 0 # number of strokes needed for this level
    # if the first element isn't 0, increase strokes by 1
    if A[1] != 0:
        strokes += 1
    # iterate from 1st element till (len(A) - 1)th element
    for i in range(1, len(A) - 2):
        # if element == 0 and next element isn't (new stroke found),
        # increase strokes
        if A[i] == 0 and A[i + 1] != 0:
            strokes += 1
    # reduce the skyline (all positive elements in A) by 1 level
    decrease(A, 1)
    return strokes + solution(A)


def is_zero(A: List[int]):
    """Checks if all elements in the input array are equal to 0 or not """
    for i in A:
        if i != 0:
            return False
    return True

def decrease(A: List[int], levels: int):
    """Decreases all positive elements in an array by [levels] units"""
    for i in range(len(A)):
        if A[i] > 0:
            A[i] -= levels
