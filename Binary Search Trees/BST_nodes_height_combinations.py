# Compute the number of Binary Search Trees 
# that can be created with n nodes and h height

# Declaring a dp-array
dp = [[-1 for _ in range(105)] for _ in range(105)]

mod = 1000000007

# Function to find the count of
# BST upto height 'H' consisting
# of 'N' nodes.
def countOfBST(N, H):

		# Base Case1 : If N == 0, return
		# 1 as a valid BST has been formed
	if (N == 0):
		return 1

		# Base Case2 : If H == 0, return true
		# if N == 1
	if (H == 0):
		return N == 1

		# If the current state has already
		# been computed, then return it.
	if (dp[N][H] != -1):
		return dp[N][H]

		# Initialize answer to 0.
	ans = 0

	# Iterate over all numbers from
	# [1, N], with 'i' as root.
	for i in range(1, N+1):

				# Call the recursive functions to
				# find count of BST of left and right
				# subtrees. Add the product of
				# both terms to the answer.
		ans += (countOfBST(i - 1, H - 1) * countOfBST(N - i, H - 1)) % mod

		# Take modulo 1000000007
		ans %= mod

		# Return ans
	dp[N][H] = ans
	return dp[N][H]

# Utility function to find the count
# of BST upto height 'H' consisting
# of 'N' nodes.
def UtilCountOfBST(N, H):

		# Initialize dp-array with -1.

		# If height is 0, return true if
		# only one node is present.
	if (H == 0):
		return (N == 1)

	# Function call.
	return (countOfBST(N, H)
			- countOfBST(N, H - 1)
			+ mod) % mod

# Driver code
if __name__ == "__main__":

	# Number of nodes
	N = 4

	# Height of tree
	H = 2

	print(UtilCountOfBST(N, H))
