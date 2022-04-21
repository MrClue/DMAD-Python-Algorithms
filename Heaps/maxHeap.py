# Python3 program to demonstrate working of heapq

from heapq import heappop, heappush, heapify

# Creating empty heap
heap = []
heapify(heap)

# heappush + print
def printPush(item):
	heappush(heap, -1 * item)

	print("Current Heap Elements: ")
	for i in heap:
		print(-1 * i, end = ' ')
	print() # new line

# Adding items to the heap using heappush
# function by multiplying them with -1
"""
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
"""
printPush(21)
printPush(18)
printPush(10)
printPush(12)
printPush(8)
printPush(9)
printPush(4)
printPush(7)
printPush(5)
printPush(2)

print() # new line

# extracting the maximum element from the heap
print("HEAP-EXTRACT-MAX: "+str(-1 * heap[0]) + "\n")
element = heappop(heap)

# printing the elements of the heap
print("The Heap Elements: ")
for i in heap:
	print(-1 * i, end = ' ')

