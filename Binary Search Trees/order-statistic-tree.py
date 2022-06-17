from platform import node


class Node:

	# Constructor to create a new node
	def __init__(self, key, value):
		self.data = key
		self.size = value
		self.left = None
		self.right = None

def insert(node, data, size):

	# 1. If the tree is empty, return a new,
	# single node
	if node is None:
		return (Node(data, size))

	else:
		# 2. Otherwise, recur down the tree
		if data <= node.data:
			node.left = insert(node.left, data, size)
		else:
			node.right = insert(node.right, data, size)

		# Return the (unchanged) node pointer
		return node

def osSelect(self, i):
	r = self.left + 1
	if i == r:
		return self
	elif i < r:
		return osSelect(self.left, i)
	else:
		return osSelect(self.right, i - r)

# Driver program
root = None
i = None
root = insert(root,10,4)
insert(root,7,2)
insert(root,12,1)
insert(root,3,1)


print ("\nOS-Search %d" %(osSelect(root,i)))