# A Python program to demonstrate common binary heap operations

# Import the heap functions from python library
from heapq import heappush, heappop, heapify

# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#			 heap invarient
# heapify - transform list into heap, in place, in linear time

# A class for Min Heap
class MinHeap:
	
	# Constructor to initialize a heap
	def __init__(self):
		self.heap = []

	def parent(self, i):
		return (i-1)//2
	
	# Inserts a new key 'k'
	def insertKey(self, k):
		heappush(self.heap, k)
		print("MIN-HEAP-INSERT: " + str(k))		

	# Decrease value of key at index 'i' to new_val
	# It is assumed that new_val is smaller than heap[i]
	def decreaseKey(self, i, new_val):
		print("DECREASE-KEY("+str(i)+", "+str(new_val)+")")
		self.heap[i] = new_val
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
			# Swap heap[i] with heap[parent(i)]
			self.heap[i] , self.heap[self.parent(i)] = (
			self.heap[self.parent(i)], self.heap[i])
			
	# Method to remove minium element from min heap
	def extractMin(self):
		print("HEAP-EXTRACT-MIN: " + str(self.heap[0]))
		return heappop(self.heap)

	# This functon deletes key at index i. It first reduces
	# value to minus infinite and then calls extractMin()
	def deleteKey(self, i):
		print("DELETE-KEY("+str(i)+")")
		self.decreaseKey(i, float("-inf"))
		self.extractMin()

	# Get the minimum element from the heap
	def getMin(self):
		#print("Current-min: " + str(self.heap[0]))
		return print("Current-min: " + str(self.heap[0])) #self.heap[0]

# Driver pgoratm to test above function
heapObj = MinHeap()
heapObj.insertKey(1)
heapObj.insertKey(3)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(10)
heapObj.insertKey(13)
heapObj.insertKey(7)
heapObj.insertKey(6)
heapObj.insertKey(17)
heapObj.insertKey(2)

"""
heapObj.extractMin()

heapObj.getMin()

heapObj.insertKey(1)

heapObj.getMin()

heapObj.decreaseKey(1, 10)
"""

print("\n"+ "Output:", end= ' ')
print(heapObj.heap)
