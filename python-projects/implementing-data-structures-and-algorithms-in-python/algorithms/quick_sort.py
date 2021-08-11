from typing import List

def quick_sort(arr: List[int], start: int, end: int):
    """Quick sort algorithm for sorting a list"""
    if start > end:
        return
    pi = partition(arr, start, end)
    # recursively call quicksort on both halves of partition index
    quick_sort(arr, start, pi - 1)
    quick_sort(arr, pi + 1, end)


def partition(arr: List[int], start: int, end: int):
    """partitions a list with the last element as pivot"""
    pivot = arr[end]
    # keep track of last index of an element smaller
    # than the pivot in subarray
    i = start - 1
    for j in range(start, end + 1):
        # swap current element with i if smaller than pivot
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # swap i + 1 with the pivot
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1 # return partition index



def main():
    arr1 = [3, 7, 1, 88, 5, 2, 7, 9, 22, 8, 1]
    print("initial list -> ", arr1)
    quick_sort(arr1, 0, len(arr1) - 1)
    print("sorted list -> ", arr1)

main()
