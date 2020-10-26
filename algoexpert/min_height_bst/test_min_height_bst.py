from .min_height_bst import minHeightBst
from .min_height_bst import BST as BST
from ..bst_exercises.validate_bst import validateBst

import pytest

class Test_minHeightBst:
    def test_example(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        num_nodes = len(array)

        bst = minHeightBst(array)
        assert validateBst(bst)
        assert self.tree_height(bst) == self.min_tree_height(num_nodes)

    def test_empty(self):
        array = []
        num_nodes = len(array)

        bst = minHeightBst(array)
        assert validateBst(bst)
        assert self.tree_height(bst) == self.min_tree_height(num_nodes)

    def min_tree_height(self, num_nodes):
        """Find the minimum height of a bst with num_nodes nodes."""
        height = 0
        while 2**height - 1 < num_nodes:
            height += 1

        return height

    def tree_height(self, head):
        """Find the height of a tree."""
        if head is None:
            return 0

        return 1 + max(
            self.tree_height(head.left),
            self.tree_height(head.right)
        )
