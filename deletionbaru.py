class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def delete_node(root, key):
    if not root:
        return root  # Tree is empty or key not found

    if key < root.key:
        root.left = delete_node(root.left, key)  # Search in the left subtree
    elif key > root.key:
        root.right = delete_node(root.right, key)  # Search in the right subtree
    else:
        # Node with the key to be deleted found
        if not root.left:
            return root.right  # Case with only a right child or no child
        elif not root.right:
            return root.left  # Case with only a left child
        # Node has two children, find the in-order successor (min value in the right subtree)
        temp = find_min(root.right)
        root.key = temp.key  # Copy the value of the in-order successor
        root.right = delete_node(root.right, temp.key)  # Delete the in-order successor
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

print("Original BST:")
inorder(root)
print()

key_to_delete = 15  # Change this to the key you want to delete
root = delete_node(root, key_to_delete)

print(f"BST after deleting {key_to_delete}:")
inorder(root)
