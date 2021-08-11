# def binary_search(arr, val):
#     # returns the index of val
#     return binary_search_util(arr, val, 0, len(arr) - 1)

# def binary_search_util(arr, val, left, right):
#     # returns the index of val recursively
#     if left > right:
#         # Element not found
#         return False

#     # mid = (left + right) // 2
#     # avoid overflow
#     mid = left + ((right - left) // 2)
#     if arr[mid] == val:
#         # Element exists in array
#         return True
#     elif arr[mid] > val:
#         # Midpoint greater than element >> search left half
#         return binary_search_util(arr, val, left, mid - 1)
#     else:
#         # Midpoint less than element >> search right half
#         return binary_search_util(arr, val, mid + 1, right)

def binary_search(arr, val):
    # iterative binary search
    left = 0
    right = len(arr) - 1

    # loop while array bounds are valid
    while (left <= right):
        mid = left + ((right - left) // 2)
        if arr[mid] == val:
            # Element exists in array
            return mid
        elif arr[mid] > val:
            # Midpoint greater than element >> search left half
            # by reducing right pointer
            right = mid - 1
        else:
            # Midpoint less than element >> search right half
            # by shifting left pointer
            left = mid + 1
    return False



def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [3, 6, 8, 9, 14, 18, 20, 30, 44, 50]
    print(binary_search(arr1, 1))
    print(binary_search(arr1, 50))
    print(binary_search(arr2, 50))
    print(binary_search(arr2, 1))

main()
