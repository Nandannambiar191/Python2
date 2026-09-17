class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the current node's data
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                print(f"Inserted {data} to the left of {self.data}")
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                print(f"Inserted {data} to the right of {self.data}")
            else:
                self.right.insert(data)
        else:
            # Duplicate value found; no action taken or handle as needed
            print(f"Value {data} already exists in the tree.")

    def print_tree(self):
        # In-order traversal to print the tree
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_tree()

"""---------------------------------------------------------------------"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None  # Renamed for PEP 8 compliance
        self.right_child = None  # Renamed for PEP 8 compliance

def insert(root, new_value):
    """Insert a new node with the given value into the BST."""
    if root is None:
        return BinaryTreeNode(new_value)
    if new_value < root.data:
        root.left_child = insert(root.left_child, new_value)
    elif new_value > root.data:
        root.right_child = insert(root.right_child, new_value)
    else:
        # Duplicate value found; you can decide how to handle it
        print(f"Value {new_value} already exists in the tree.")
    return root

def delete_tree(root):
    """Delete all nodes of the tree by removing references."""
    if root:
        # Delete left subtree
        delete_tree(root.left_child)
        root.left_child = None  # Remove reference to left child
        # Delete right subtree
        delete_tree(root.right_child)
        root.right_child = None  # Remove reference to right child
        # Remove data reference
        print(f"Deleting Node: {root.data}")
        root.data = None  # Optional: Remove data reference

# Build the tree
root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)

print("Deleting all the elements of the binary tree.")
delete_tree(root)
root = None  # Remove reference to the root node

"""---------------------------------------------------------------------"""
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, new_value):
        """Insert a new node with the given value into the BST."""
        if new_value < self.data:
            if self.left_child is None:
                self.left_child = BinaryTreeNode(new_value)
                print(f"Inserted {new_value} to the left of {self.data}")
            else:
                self.left_child.insert(new_value)
        elif new_value > self.data:
            if self.right_child is None:
                self.right_child = BinaryTreeNode(new_value)
                print(f"Inserted {new_value} to the right of {self.data}")
            else:
                self.right_child.insert(new_value)
        else:
            # Duplicate value found; not inserted
            print(f"Value {new_value} already exists in the tree.")

    def search(self, key):
        """Search for a node with the specified key in the BST."""
        if self.data == key:
            print(f"Found {key}")
            return True
        elif key < self.data:
            if self.left_child is not None:
                return self.left_child.search(key)
            else:
                print(f"Key not found in the tree.")
                return False
        else:  # key > self.data
            if self.right_child is not None:
                return self.right_child.search(key)
            else:
                print(f"Key not found in the tree.")
                return False

# Example usage
if __name__ == "__main__":
    root = BinaryTreeNode(13)
    root.insert(10)
    root.insert(25)
    root.insert(6)
    root.insert(14)
    root.insert(20)
    root.insert(60)

    # Searching for nodes
    root.search(14)  # Should find the node
    root.search(99)  # Should report that the node is not found
    root.search(6)
    root.search(88)