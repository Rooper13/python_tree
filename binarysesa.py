class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_in_bst(root, target):
    if not root:
        return None  # Tree is empty or target is not found

    if root.key == target:
        return root  # Found the target value

    if target < root.key:
        return search_in_bst(root.left, target)  # Recursively search in the left subtree

    return search_in_bst(root.right, target)  # Recursively search in the right subtree

# Example usage:
# Create a sample binary search tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

target_value = 7  # Change this to the value you want to search for

result = search_in_bst(root, target_value)

if result:
    print(f"Found {target_value} in the BST")
else:
    print(f"{target_value} not found in the BST")
