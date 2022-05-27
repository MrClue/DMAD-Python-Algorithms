from itertools import count
from operator import index
from numpy import array

def countingSort(array):
    size = len(array)
    output = [0] * size

    c1 = []
    c2 = []
    c_final = []

    # Initialize count array
    count = [0] * size

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Printing C1
    for i in range(0, size - 1):
        c1.append(count[i])
    
    print("C: (stored counts of A)")
    print(c1)

    # Store the cummulative count
    for i in range(1, size):
        count[i] += count[i - 1]

    # Printing C2
    for i in range(0, size - 1):
        c2.append(count[i])
    
    print("C: (cummulative count)")
    print(c2,"\n")

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
        

# OUTPUT
data = [3, 1, 4, 3, 5, 0, 3, 1]

print("A: (start input)")
print(data)

countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
