arr = [4, 10, 3, 5, 1, 6, 2]

print("Original array:"+"\n" + str(arr) + "\n")

def heapify(arr, n, i): 
    largest = i # set largest as root
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if (l < n and arr[i] < arr[l]): 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if (r < n and arr[largest] < arr[r]): 
        largest = r 
  
    # Change root, if needed 
    if (largest != i): 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)
  
# function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a heap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i)
        #print("Build heap "+str(i)+": "+str(arr))
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)
        print("Extract heap "+str(i)+": " + str(arr)) # test - visualise
  
# Driver code to test above 

heapSort(arr) # perform sort
print ("\n"+"Sorted array:"+"\n" + str(arr))
