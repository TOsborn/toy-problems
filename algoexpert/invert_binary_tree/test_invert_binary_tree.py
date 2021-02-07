import pytest

from .invert_binary_tree import BinaryTree, invertBinaryTree


def test_example():
    tree = {i: BinaryTree(i) for i in range(1, 10)}
    root = tree[1]

    tree[1].left, tree[1].right = tree[2], tree[3]
    tree[2].left, tree[2].right = tree[4], tree[5]
    tree[3].left, tree[3].right = tree[6], tree[7]
    tree[4].left, tree[4].right = tree[8], tree[9]


    r_tree = {i: BinaryTree(i) for i in range(1, 10)}
    r_root = r_tree[1]

    r_tree[1].right, r_tree[1].left = r_tree[2], r_tree[3]
    r_tree[2].right, r_tree[2].left = r_tree[4], r_tree[5]
    r_tree[3].right, r_tree[3].left = r_tree[6], r_tree[7]
    r_tree[4].right, r_tree[4].left = r_tree[8], r_tree[9]


    assert invertBinaryTree(root) == r_root
