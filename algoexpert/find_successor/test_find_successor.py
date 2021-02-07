from .find_successor import BinaryTree, findSuccessor

def test_findSuccessor_example():
    tree = {i: BinaryTree(i) for i in range(1, 7)}
    root = tree[1]

    tree[1].left, tree[1].right = tree[2], tree[3]
    tree[2].left, tree[2].parent, tree[2].right = tree[4], tree[1], tree[5]
    tree[3].parent = tree[1]
    tree[4].left, tree[4].parent = tree[6], tree[2]
    tree[5].parent = tree[2]
    tree[6].parent = tree[4]


    assert findSuccessor(root, tree[6]) is tree[4]
    assert findSuccessor(root, tree[4]) is tree[2]
    assert findSuccessor(root, tree[2]) is tree[5]
    assert findSuccessor(root, tree[5]) is tree[1]
    assert findSuccessor(root, tree[1]) is tree[3]
    assert findSuccessor(root, tree[3]) is None