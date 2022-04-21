# Python3 program to demonstrate working of heapq

from heapq import heappop, heappush, heapify

# Creating empty heap
heap = []
heapify(heap)

# Adding items to the heap using heappush
# function by multiplying them with -1
heappush(heap, -1 * 10)
heappush(heap, -1 * 8)
heappush(heap, -1 * 6)
heappush(heap, -1 * 3)
heappush(heap, -1 * 7)
heappush(heap, -1 * 4)
heappush(heap, -1 * 5)
heappush(heap, -1 * 1)
heappush(heap, -1 * 2)
heappush(heap, -1 * 9)

# printing the value of maximum element
print("Head value of heap: "+str(-1 * heap[0]))

element = heappop(heap)

# printing the elements of the heap
print("The heap elements: ")
for i in heap:
	print(-1 * i, end = ' ')


