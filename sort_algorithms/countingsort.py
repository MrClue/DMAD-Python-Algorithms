from itertools import count
from operator import index

from numpy import array

def countingSort(array):
    size = len(array)
    output = [0] * size
    c_start = []
    c_final = []

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Printing working array C
    for i in range(0, size - 1):
        c_start.append(count[i])
    
    print("Start working array C")
    print(c_start)
    print("\t")

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

    # Printing working array C
    for i in range(0, size - 1):
        c_final.append(count[i])
    
    print("Final working array C")
    print(c_final)
        

data = [3,1,4,3,5,0,3,1]
print("Start input")
print(data)
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)