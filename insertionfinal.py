class NewNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None 

def inorder(temp):
    if not temp:
        return

    inorder(temp.left)
    print(temp.key, end=" ")  # Added space for better readability
    inorder(temp.right)

def insert(temp, key):
    if not temp:
        root = NewNode(key)
        return
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = NewNode(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = NewNode(key)
            break
        else:
            q.append(temp.right)

if __name__ == '__main__':
    root = NewNode(10)
    root.left = NewNode(11)
    root.left.left = NewNode(18)
    root.right = NewNode(9)
    root.right.left = NewNode(12)
    root.right.right = NewNode(13)

    print("Inorder traversal before insertion: ", end="")
    inorder(root)

    key = 29
    insert(root, key)

    print("\nInorder traversal after insertion: ", end="")
    inorder(root)
