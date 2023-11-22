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

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L-- ")
            print_tree(root.right, level + 1, "R-- ")

# Example usage:
root_node = None
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for key in keys:
    root_node = insert(root_node, key)

print_tree(root_node)
