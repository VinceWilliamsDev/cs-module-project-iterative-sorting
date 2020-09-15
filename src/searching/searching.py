def linear_search(arr, target):
    # Your code here
    i = 0
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
        else:
            i += 1


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    high = len(arr) - 1
    low = 0
    while low <= high:
        midpoint = (low + high) // 2
        if arr[midpoint] > target:
            high = midpoint - 1
        elif arr[midpoint] < target:
            low = midpoint + 1
        else:
            return midpoint

    return -1  # not found
