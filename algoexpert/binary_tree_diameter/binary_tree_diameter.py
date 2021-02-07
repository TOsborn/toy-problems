def binaryTreeDiameter(tree):
    """Find the diameter of a tree."""
    def helper(tree):
        if tree is None:
            return -1, 0
        
        left_depth, left_diameter = helper(tree.left)
        right_depth, right_diameter = helper(tree.right)

        depth = 1 + max(left_depth, right_depth)

        thru_diameter = left_depth + right_depth + 2
        diameter = max(left_diameter, right_diameter, thru_diameter)

        return depth, diameter

    return helper(tree)[1]



# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
