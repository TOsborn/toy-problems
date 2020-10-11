from bst import BST

class _BSTValidator:
    def validateBst(self, tree):
        self._populateMinMaxDicts(tree)

        return self._validateHelper(tree)

    def _validateHelper(self, tree):
        if tree is None:
            return True

        return (self._validNode(tree)
            and self._validateHelper(tree.left)
            and self._validateHelper(tree.right))

    def _validNode(self, tree):
        if tree is None:
            return True

        return (self._max_val[tree.left]
                < tree.value <= self._min_val[tree.right])

    def _populateMinMaxDicts(self, tree):
        self._min_val = {None: float('inf')}
        self._max_val = {None: -float('inf')}

        self._updateMinDict(tree)
        self._updateMaxDict(tree)

    def _updateMinDict(self, tree):
        if tree is None:
            return float('inf')
        
        self._min_val[tree] = min(
            tree.value,
            self._updateMinDict(tree.left),
            self._updateMinDict(tree.right),
        )

        return self._min_val[tree]

    def _updateMaxDict(self, tree):
        if tree is None:
            return -float('inf')

        self._max_val[tree] = max(
            tree.value,
            self._updateMaxDict(tree.left),
            self._updateMaxDict(tree.right)
        )

        return self._max_val[tree]

def validateBst(tree):
    """Check that tree is a valid binary search tree."""
    return _BSTValidator().validateBst(tree)

