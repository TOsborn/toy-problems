def minHeightBst(array):
    def rec(array):
        if array == []:
            return None

        median = len(array) // 2
        head = BST(array[median])
        head.left = rec(array[:median])
        head.right = rec(array[median+1:])

        return head


    array = sorted(array)
    return rec(array)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
