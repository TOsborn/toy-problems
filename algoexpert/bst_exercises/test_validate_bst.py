import validate_bst
from bst import BST

from random import shuffle
import pytest

def test_valid():
    root = BST(2)
    root.left = BST(1)
    root.right = BST(3)

    assert validate_bst.validateBst(root) is True

def test_invalid():
    root = BST(1)
    root.left = BST(2)
    root.right = BST(3)

    assert validate_bst.validateBst(root) is False

def test_equal_valid():
    root = BST(2)
    root.left = BST(1)
    root.right = BST(2)

    assert validate_bst.validateBst(root) is True

def test_equal_invalid():
    root = BST(2)
    root.left = BST(2)
    root.right = BST(3)

    assert validate_bst.validateBst(root) is False

def test_single_node():
    root = BST(1)

    assert validate_bst.validateBst(root) is True

def test_two_layers_valid():
    root = BST(3)
    root.left = BST(2)
    root.left.left = BST(1)

    assert validate_bst.validateBst(root) is True

def test_layer_down_invalid():
    root = BST(2)
    root.left = BST(1)
    root.left.right = BST(2)

    assert validate_bst.validateBst(root) is False

def test_random_large_bst_valid():
    root = _construct_bst(list(range(100)))

    assert validate_bst.validateBst(root) is True

def test_random_large_bst_invalid():
    root = _construct_bst(list(range(100)))
    if root.left:
        root.left.value = 100
    else:
        assert root.right
        root.right.value = -1

    assert validate_bst.validateBst(root) is False

def test_two_layers_down_invalid():
    root = BST(3)
    root.left = BST(2)
    root.left.left = BST(1)
    root.left.left.right = BST(0)

    assert validate_bst.validateBst(root) is False

def _construct_bst(values):
    if values == []:
        return None

    values = values.copy()
    shuffle(values)

    root = BST(values[0])
    for val in values[1:]:
        root.insert(val)

    return root


