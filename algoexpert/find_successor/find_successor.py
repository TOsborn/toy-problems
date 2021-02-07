class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    """Find the successor of node in an in-order traversal."""
    if node.right:
        return leftmostDescendant(node.right)

    if node.parent and node.parent.left is node:
        return node.parent
    
    while node.parent and node.parent.right is node:
        node = node.parent

    return node.parent


def leftmostDescendant(node):
	while node.left:
		node = node.left
		
	return node
