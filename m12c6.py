class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_nodes_with_one_child(root, single_child_nodes=None):
    if single_child_nodes is None:
        single_child_nodes = []

    if not root:
        return single_child_nodes

    # Check if the current node has exactly one child
    if (root.left and not root.right) or (root.right and not root.left):
        single_child_nodes.append(root)

    # Recurse on the left and right subtrees
    find_nodes_with_one_child(root.left, single_child_nodes)
    find_nodes_with_one_child(root.right, single_child_nodes)

    return single_child_nodes

def find_paths_in_range(root, low, high, current_path=None, current_sum=0, valid_paths=None):
    if valid_paths is None:
        valid_paths = []

    if current_path is None:
        current_path = []

    if root is None:
        return valid_paths

    # Include the current node in the path and add its value to the sum
    current_path.append(root.val)
    current_sum += root.val

    # If it's a leaf node, check if the current sum is within the range
    if root.left is None and root.right is None:
        if low <= current_sum <= high:
            # Append a copy of the current path to valid_paths
            valid_paths.append(list(current_path))
    else:
        # Recurse on the left and right children
        find_paths_in_range(root.left, low, high, current_path, current_sum, valid_paths)
        find_paths_in_range(root.right, low, high, current_path, current_sum, valid_paths)

    # Backtrack: Remove the current node before returning to the caller
    current_path.pop()

    return valid_paths

def main():
    # Construct the binary tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(7)
    root.right.left = Node(8)
    root.right.right = Node(6)

    # Find and collect nodes with exactly one child
    single_child_nodes = find_nodes_with_one_child(root)

    # Print nodes with exactly one child
    if not single_child_nodes:
        print(-1)
    else:
        print("Nodes with exactly one child:")
        for node in single_child_nodes:
            print(node.val, end=" ")
        print()

    # Define the sum range
    low = 14
    high = 21

    # Find and print all root-to-leaf paths within the sum range
    valid_paths = find_paths_in_range(root, low, high)
    if valid_paths:
        print(f"\nRoot-to-leaf paths with sum in range [{low}, {high}]:")
        for path in valid_paths:
            print(" -> ".join(map(str, path)))
    else:
        print(f"\nThere are no root-to-leaf paths with sum in range [{low}, {high}].")

if __name__ == "__main__":
    main()


"""---------------------------------------------------------------------"""

class newNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None

def traverse(root, tilt):
    if (not root):
        return 0

    left = traverse(root.left, tilt)
    right = traverse(root.right, tilt)

    tilt[0] += abs(left - right)

    return left + right + root.val

def Tilt(root):
    tilt = [0]
    traverse(root, tilt)
    return tilt[0]

if __name__ == '__main__':
    root = None
    root = newNode(4)
    root.left = newNode(2)
    root.right = newNode(9)
    root.left.left = newNode(3)
    root.left.right = newNode(8)
    root.right.right = newNode(7)
    print("The Tilt of whole tree is",Tilt(root))

"""---------------------------------------------------------------------"""

IMIN = -2147483648
IMAX = 2147483647
def largestBst(root):
    if root==None:
        return IMAX,IMIN,0
    if (root.left==None and root.right==None):
        return root.data,root.data,1

    left=largestBst(root.left)
    right=largestBst(root.right)

    ans=[0,0,0]

    if left[1]<root.data and right[0]>root.data:
        ans[0]=min(left[0],right[0],root.data)
        ans[1]=max(right[1],left[1],root.data)
        ans[2]=1+left[2]+right[2]
        return ans

    ans[0]=IMIN
    ans[1]=IMAX
    ans[2]=max(left[2],right[2])
    return ans

def largestBstUtil(root):

    return largestBst(root)[2]

import sys
sys.setrecursionlimit(1000000)
from collections import deque

class newNode:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

if __name__ == '__main__':
    root = newNode(50)
    root.left = newNode(75)
    root.right = newNode(45)
    root.left.left = newNode(40)
    print("Size of the largest BST is", largestBstUtil(root))