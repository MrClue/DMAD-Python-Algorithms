""" 
Merge-Sort implemented using the example from Cormen et al., page 31 & 34

Array index starts at 1 (!)
"""

def merge(A, p, q, r):
    #decide the length of the two lists
    n1 = q-p+1
    n2 = r-q
    #create the left and right arrays
    L=[]
    R=[]
    #divide the the array to the corresponding list in a for loop
    for i in range(n1):
        L.append(A[p-1+i])
    for j in range(n2):
        R.append(A[q+j])
    #create the index pointer for the two arrays
    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    #update the merged array
    for k in range(p-1,r):
        #copy the left array to the merged array when the left element is smaller or the same 
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        #copy the right array to the merged array when the right element is smaller
        else:
            A[k] = R[j]
            j+=1
    return A

def merge_sort(A,p,r):
    #check if r is larger than p, if r and q are the same number, we cannot divide again -> the base case.
    if p < r:
        #divide the list by two
        q = (p+r)//2
        #continue to merge sort the first sub-array
        merge_sort(A,p,q)
        #continue to merge sort the second sub-array
        merge_sort(A,q+1,r)
        #merge the two sorted algorithms
        merge(A,p,q,r)
    #return the original list A
    return(A)

#check if merge sort works
A=[8,6,1,5,1,9,4,9]
# p, q, r
left = 1
#middle = 2 
right = 4

#merge(A, left, middle, right)
merge_sort(A, left, right)

print(A)
