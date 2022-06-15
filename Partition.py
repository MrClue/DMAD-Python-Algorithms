# This Python file uses the following encoding: utf-8

"""
    Implementing Partition(A, p, r)

    Runs partition from index [p] to the pivot index [r]
    Index start from 0
"""

def partition(A, p, r):
    
    # pivot is typically right-most element
    pivot = A[r]

    # pointer for greater element
    i = p - 1

    # traverse through all elements and compare each with pivot
    for j in range(p, r):
        if A[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1

            # swapping element at i with element at j
            (A[i], A[j]) = (A[j], A[i])

    # swap pivot element with the greater element specified by i
    (A[i + 1], A[r]) = (A[r], A[i + 1])

    # return the position from where partition is done
    #return i + 1
    return A # hvis opgaven bare siger: udfør PARTITION(A, q, r)


arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print(partition(arr, 0, 11))