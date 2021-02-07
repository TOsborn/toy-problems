from .binary_tree_diameter import BinaryTree, binaryTreeDiameter

def test_binaryTreeDiameter_example():
    tree = {i: BinaryTree(i) for i in range(1, 10)}
    root = tree[1]

    tree[1].left, tree[1].right = tree[3], tree[2]

    tree[3].left, tree[3].right = tree[7], tree[4]
    tree[4].right = tree[5]
    tree[5].right = tree[6]

    tree[7].right = tree[8]
    tree[8].right = tree[9]

    assert binaryTreeDiameter(root) == 6