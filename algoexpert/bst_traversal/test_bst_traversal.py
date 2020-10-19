from bst_traversal import BST, inOrderTraverse, preOrderTraverse, \
    postOrderTraverse


one = BST(1)
two = BST(2)
three = BST(3)
four = BST(4)
five = BST(5)

def setup():
    one.left = two
    one.right = three

    two.left = four
    two.right = five

    tree = one

    array = []

    return tree, array

def test_inOrderTraverse():
    tree, array = setup()
    inOrderTraverse(tree, array)

    assert array == [4, 2, 5, 1, 3]


def test_preOrderTraverse():
    tree, array = setup()
    preOrderTraverse(tree, array)

    assert array == [1, 2, 4, 5, 3]


def test_postOrderTraverse():
    tree, array = setup()
    postOrderTraverse(tree, array)

    assert array == [4, 5, 2, 3, 1]
