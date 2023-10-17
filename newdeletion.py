class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._find_min(root.right)
            root.right = self._delete(root.right, root.key)

        return root

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.key

# Usage example:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("BST before deletion:")
# Perform in-order traversal to print the tree
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

inorder_traversal(bst.root)
print()

bst.delete(30)
print("BST after deleting 30:")
inorder_traversal(bst.root)
