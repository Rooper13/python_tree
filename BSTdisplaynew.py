class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def display_bst(root):
    if root:
        display_bst(root.left)
        print(root.val, end=" ")
        display_bst(root.right)

# Example usage:
root_node = None
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for key in keys:
    root_node = insert(root_node, key)

display_bst(root_node)
