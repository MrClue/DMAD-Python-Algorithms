# Python3 program to construct all unique
# BSTs for keys from 1 to n

# Binary Tree Node
""" A utility function to create a
new BST node """
class newNode:

	# Construct to create a newNode
	def __init__(self, item):
		self.key=item
		self.left = None
		self.right = None

# A utility function to do preorder
# traversal of BST
def preorder(root) :

	if (root != None) :
	
		print(root.key, end = " " )
		preorder(root.left)
		preorder(root.right)
	
# function for constructing trees
def constructTrees(start, end):

	list = []

	""" if start > end then subtree will be
		empty so returning None in the list """
	if (start > end) :
	
		list.append(None)
		return list
	
	""" iterating through all values from
		start to end for constructing
		left and right subtree recursively """
	for i in range(start, end + 1):
	
		""" constructing left subtree """
		leftSubtree = constructTrees(start, i - 1)

		""" constructing right subtree """
		rightSubtree = constructTrees(i + 1, end)

		""" now looping through all left and
			right subtrees and connecting
			them to ith root below """
		for j in range(len(leftSubtree)) :
			left = leftSubtree[j]
			for k in range(len(rightSubtree)):
				right = rightSubtree[k]
				node = newNode(i) # making value i as root
				node.left = left # connect left subtree
				node.right = right # connect right subtree
				list.append(node) # add this tree to list
	return list

# Driver Code
if __name__ == '__main__':

	# Construct all possible BSTs
	totalTreesFrom1toN = constructTrees(1, 4)

	""" Printing preorder traversal of
		all constructed BSTs """
	print("Preorder traversals of all",
				"constructed BSTs are")
	for i in range(len(totalTreesFrom1toN)):
		preorder(totalTreesFrom1toN[i])
		print()


