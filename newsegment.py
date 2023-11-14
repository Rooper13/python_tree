class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# Example usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print("Original array:", arr)
print("Segment tree:", seg_tree.tree)

# Update the element at index 2 to 8
seg_tree.update(2, 8)
print("Updated segment tree:", seg_tree.tree)

# Query the sum of elements in the range [1, 4]
query_result = seg_tree.query(1, 4)
print("Sum in range [1, 4]:", query_result)
