"""
Much simpler way to count inversions in array
"""

def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        # compare to next index
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count

# Driver Code
arr = [5, 1, 3, 7, 2, 3, 8, 6, 1]
n = len(arr)
print("Number of inversions are", getInvCount(arr, n))

