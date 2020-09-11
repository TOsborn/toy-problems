from random import shuffle

class BST:
    """Binary search tree.
    
    Supports insertion and removal of elements, as well as containment
    check.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insert a new value."""
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            assert self.value <= value
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    def contains(self, value):
        """Check if a value exists in the tree."""
        if self.value == value:
            contains = True
        else:
            left_or_right = ['left', 'right'][self.value <= value]
            child = getattr(self, left_or_right)
            if child is None:
                contains = False
            else:
                contains = child.contains(value)

        return contains
        

    def remove(self, value):
        """Remove an instance of a value."""
        node, parent, which_child = self._get_node_with_parent(value)
        absent_value = (node is None)
        if not absent_value:
            is_leaf = (node.left is node.right is None)
            is_single_node_tree = (node is self and is_leaf)

        if absent_value or is_single_node_tree:
            pass
        elif node.right:
            leftmost_right = node._pop_leftmost_right_descendant()
            node.value = leftmost_right.value
        elif node.left:
            node._replace_attributes(node.left)
        else:
            assert is_leaf
            setattr(parent, which_child, None)

        return self

    def _get_node_with_parent(self, value):
        if value == self.value:
            node, parent, which_child = self, None, None
        elif self.left is self.right is None:
            node, parent, which_child = None, None, None
        else:
            left_or_right = ['left', 'right'][self.value <= value]
            next_descendant = getattr(self, left_or_right)
            if next_descendant is None:
                node, parent, which_child = None, None, None
            elif next_descendant.value == value:
                node = next_descendant
                parent = self
                which_child = left_or_right
            else:
                node, parent, which_child = \
                    next_descendant._get_node_with_parent(value)
        
        return node, parent, which_child

    def _pop_leftmost_right_descendant(self):
        parent, node = self, self.right
        while node.left:
            parent, node = node, node.left

        if parent is self:
            parent.right = node.right
        else:
            parent.left = node.right
        
        return node
        

    def _replace_attributes(self, other):
        self.value = other.value
        self.left = other.left
        self.right = other.right

    def _traverse(self):
        if self.left:
            yield from self.left._traverse()

        yield self.value
        if self.right:
            yield from self.right._traverse()

    def _flatten(self):
        return list(self._traverse())

    def _construct_bst(self, values):
        if values == []:
            return None

        values = values.copy()
        shuffle(values)

        root = BST(values[0])
        for val in values[1:]:
            root.insert(val)

        return root
