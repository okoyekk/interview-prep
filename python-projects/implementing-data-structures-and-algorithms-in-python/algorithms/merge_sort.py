def merge_sort(arr):
    """Merge sort algorithm for sorting list"""
    if len(arr) > 1:
        # divide array into 2 halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # recursively call mergesort on both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        # compare left and right subarrays and update initial array
        # with appropriate value from either (merging)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # update initial array with leftover elements
        # (case where right and left subarrays don't have the same length)
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1



def main():
    arr1 = [3, 7, 1, 88, 5, 2, 7, 9, 22, 8, 1]
    print("initial list -> ", arr1)
    merge_sort(arr1)
    print("sorted list -> ", arr1)

main()
