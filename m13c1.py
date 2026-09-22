# Python program to implement
# inorder traversal of BST

# Given Node node
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to create a new BST node
def newNode(item):
	temp = Node(item)
	temp.key = item
	temp.left = temp.right = None
	return temp

# Function to insert a new node with
# given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return newNode(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the node pointer
	return node

# Function to do inorder traversal of BST
def inorder(root):
	if root:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

# Driver Code
if __name__ == '__main__':
	
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	# / \ / \
	# 20 40 60 80
	root = None

	# Creating the BST
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	# Function Call
	inorder(root)

"""---------------------------------------------------------------------"""

# A O(n^2) Python3 program for
# construction of BST from preorder traversal

# A binary tree node


class Node():

	# A constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# constructTreeUtil.preIndex is a static variable of
# function constructTreeUtil

# Function to get the value of static variable
# constructTreeUtil.preIndex
def getPreIndex():
	return constructTreeUtil.preIndex

# Function to increment the value of static variable
# constructTreeUtil.preIndex


def incrementPreIndex():
	constructTreeUtil.preIndex += 1

# A recursive function to construct Full from pre[].
# preIndex is used to keep track of index in pre[[].


def constructTreeUtil(pre, low, high):

		# Base Case
	if(low > high):
		return None

	# The first node in preorder traversal is root. So take
	# the node at preIndex from pre[] and make it root,
	# and increment preIndex
	root = Node(pre[getPreIndex()])
	incrementPreIndex()

	# If the current subarray has only one element,
	# no need to recur
	if low == high:
		return root

	r_root = -1

	# Search for the first element greater than root
	for i in range(low, high+1):
		if (pre[i] > root.data):
			r_root = i
			break

	# If no elements are greater than the current root,
	# all elements are left children
	# so assign root appropriately
	if r_root == -1:
		r_root = getPreIndex() + (high - low)

	# Use the index of element found in preorder to divide
	# preorder array in two parts. Left subtree and right
	# subtree
	root.left = constructTreeUtil(pre, getPreIndex(), r_root-1)

	root.right = constructTreeUtil(pre, r_root, high)

	return root

# The main function to construct BST from given preorder
# traversal. This function mainly uses constructTreeUtil()


def constructTree(pre):
	size = len(pre)
	constructTreeUtil.preIndex = 0
	return constructTreeUtil(pre, 0, size-1)


def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print(root.data, end=' ')
	printInorder(root.right)



pre = [10, 5, 1, 7, 40, 50]

root = constructTree(pre)

printInorder(root)


