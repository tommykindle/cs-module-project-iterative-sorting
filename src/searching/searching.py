def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0  # define left pointer at 0th index
    right = len(arr) - 1  # define right pointer at ending index of array
    while left <= right:  # while left is less than or equal to right
        # find the middle by adding the left pointer index to the right divide by two and round down
        middle = (left + right) // 2
        # set our possible match to be array at index of middle
        possibleMatch = arr[middle]
        if target == possibleMatch:  # if the target is equal to our possible match
            return middle  # return middle
        elif target < possibleMatch:  # if are target is less than our possible match
            right = middle - 1  # set the right pointer to one less index than middle to eliminate the right hand side of the array
        else:
            left = middle + 1  # set the left pointer to one more than the middle to eliminate the left hand side of the array

    return -1  # not found
