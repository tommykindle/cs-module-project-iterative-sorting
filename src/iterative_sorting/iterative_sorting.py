# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    currentIdx = 0  # first number of unsorted sublist
    while currentIdx < len(arr) - 1:  # assume the last number is in place
        smallestIdx = currentIdx
        # iterate through sublist starting at the second index going through the array
        for i in range(currentIdx + 1, len(arr)):
            # if the smallest index is greater than the current index update the smallest index to the current index in the loop
            if arr[smallestIdx] > arr[i]:
                smallestIdx = i
        # call helper function to swap smallest index with the current index
        swap(currentIdx, smallestIdx, arr)
        currentIdx += 1

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    isSorted = False  # assume the arr is not sorted
    # set a counter to reduce traversing the entire array on each pass.
    counter = 0
    while not isSorted:
        isSorted = True  # temporarly assume the array is sorted until for loop runs
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:  # check to see if positon before is greater than next position if so
                # run swap helper function to switch index of i with index of i +1
                swap(i, i + 1, arr)
                isSorted = False  # set isSorted back to false due to making a swap
        counter += 1  # increment counter by one so that the second pass does not go over the entire array again

    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
