from solution import BST

import pytest
from collections import namedtuple
from random import shuffle

class TestBST:
    flattened_tree = [1, 2, 5, 5, 10, 13, 14, 15, 22]

    def test_failed(self):
        root = BST(10)
        root.right = BST(15)
        root.left = BST(5)

        root.remove(10)
        assert root._flatten() == [5, 15]

        root = BST(10)
        root.left = BST(5)

        assert root.value == 10
        assert root.left.value == 5

        root = root.insert(15)
        assert root._flatten() == [5, 10, 15]
        
        assert root.value == 10
        assert root.left.value == 5
        assert root.right.value == 15

        root = root.remove(5)
        assert root._flatten() == [10, 15]

        assert root.value == 10
        assert root.left is None
        assert root.right.value == 15

        root.remove(10)
        assert root._flatten() == [15]

        assert root.value == 15
        assert root.left == None
        assert root.right == None

    def test_insert(self):
        root = self._construct_bst(self.flattened_tree)

        root = root.insert(12)
        assert root._flatten() == [1, 2, 5, 5, 10, 12, 13, 14, 15, 22]

    def test_remove(self):
        root = self._construct_bst(self.flattened_tree)

        root = root.remove(5)
        assert root._flatten() == [1, 2, 5, 10, 13, 14, 15, 22]

        values = [1, 2, 5, 10, 13, 14, 15, 22]
        values_root_excluded = [val for val in values if val != root.value]
        root = root.remove(root.value)
        assert root._flatten() == values_root_excluded

        root = BST(1)
        root = root.remove(1)
        assert root._flatten() == [1]

    def test_contains(self):
        root = self._construct_bst(self.flattened_tree)

        assert root.contains(15) == True
        assert root.contains(10) == True
        assert root.contains (22) == True

        assert root.contains(0) == False
        assert root.contains(11) == False
        assert root.contains(23) == False

    def _construct_bst(self, values):
        values = values.copy()
        shuffle(values)

        root = BST(values[0])
        for val in values[1:]:
            root.insert(val)

        return root
