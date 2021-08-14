from typing import List
from itertools import combinations_with_replacement

def solution(A: List[int], F: int, M: int) -> List[int]:
    # validate input
    if M < 1 or M > 6:
        return [0]

    # get sum of forgotten elements
    forgotten_sum = (M * (len(A) + F)) - sum(A)
    # get average of forgotten elements
    forgotten_mean = forgotten_sum / F
    # check if mean is possible with input
    if forgotten_mean < 1 or forgotten_mean > 6:
        return [0]
    # check if forgotten_mean is perfect (whole number),
    # in this case return an array of F elements where
    # all elements are forgotten_mean
    if forgotten_mean == round(forgotten_mean):
        return [round(forgotten_mean)] * F
    else:
        # get all combinations of numbers from 1 to 6 where their average == forgotten_mean
        # naive implementation
        sides = [1, 2, 3, 4, 5, 6]
        missing_combinations = list(combinations_with_replacement(sides, F))
        for arr in missing_combinations:
            if sum(arr) == forgotten_sum:
                return arr
    return [0]

def main():
    print(solution([3, 2, 4, 3], 2, 4))

main()
