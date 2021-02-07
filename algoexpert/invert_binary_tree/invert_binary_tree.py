def invertBinaryTree(tree):
    """Invert a binary tree.

    For each node in the tree, swap its left node for its right node.
    """
    if tree is None:
        return None
    
    tree.left, tree.right = invertBinaryTree(tree.right), invertBinaryTree(tree.left)

    return tree


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        if other is None:
            return False

        return (self.value == other.value
                and self.left == other.left
                and self.right == other.right)
