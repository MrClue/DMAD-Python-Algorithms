"""
Modified version of Merge-Sort to count the number of inversions in linear time 
"""

def merge(A, p, q, r):
    #decide the length of the two lists
    n1 = q - p + 1
    n2 = r - q
    
    #create the left and right arrays
    L=[]
    R=[]
    
    #divide the the array to the corresponding list in a for loop
    for i in range(n1):
        L.append(A[p - 1 + i])
    for j in range(n2):
        R.append(A[q + j])
    
    #create the index pointer for the two arrays
    L.append(float("inf"))
    R.append(float("inf"))
    
    i = 0
    j = 0
    inversions = 0
    
    #update the merged array
    for k in range(p - 1, r):
        #copy the left array to the merged array when the left element is smaller or the same 
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        #copy the right array to the merged array when the right element is smaller
        else:
            inversions += (n1 - i) #(n1 - i + 1)
            A[k] = R[j]
            j += 1
    
    return inversions

def count_inversions(A,p,r):
    #check if r is larger than p, if r and q are the same number, we cannot divide again -> the base case.
    if p >= r:
        return 0
    
    #divide the list by two
    q = (p+r) // 2
        
    #continue to merge sort the first sub-array + count inversions
    left = count_inversions(A,p,q)
        
    #continue to merge sort the second sub-array + count inversions
    right = count_inversions(A,q+1,r)
        
    #merge the two sorted algorithms + count inversions
    inversions = left + right + merge(A,p,q,r)

    #return the number of inversions
    return inversions

# Driver Code
arr = [5, 1, 3, 7, 2, 3, 8, 6, 1]
# p, q, r
left = 1 # lower bound
right = len(arr) # or set upper bound, eg. 5

print(count_inversions(arr, left, right))