from .bst import BST

def validateBst(tree):
    """Check that tree is a valid binary search tree."""
    def rec(tree, min_value, max_value):
        if tree is None:
            return True
        
        if not min_value <= tree.value < max_value:
            return False

        left_is_valid = rec(tree.left, min_value, tree.value)
        right_is_valid = rec(tree.right, tree.value, max_value)

        return left_is_valid and right_is_valid

    return rec(tree, -float('inf'), float('inf'))

#################################

def validateBst2(tree):
    """Check that tree is a valid binary search tree."""
    def rec(tree):
        if tree is None:
            return True, float('inf'), -float('inf')

        left_is_valid, left_min_val, left_max_val = rec(tree.left)
        right_is_valid, right_min_val, right_max_val = rec(tree.right)

        root_is_valid = (left_max_val < tree.value <= right_min_val)
        is_valid = left_is_valid and right_is_valid and root_is_valid

        min_val = min(tree.value, left_min_val)
        max_val = max(tree.value, right_max_val)

        return is_valid, min_val, max_val

    is_valid, _, _ = rec(tree)
    
    return is_valid

####################################

def validateBst3(tree):
    """Check that tree is a valid binary search tree."""
    is_valid, _, _ = _validateBstHelper(tree)

    return is_valid

def _validateBstHelper(tree):
    """Return (is_valid, min_val, max_val)."""
    if tree is None:
        return True, float('inf'), -float('inf')

    left_is_valid, left_min_val, left_max_val = _validateBstHelper(tree.left)
    right_is_valid, right_min_val, right_max_val = _validateBstHelper(tree.right)

    root_is_valid = (left_max_val < tree.value <= right_min_val)
    is_valid = left_is_valid and right_is_valid and root_is_valid

    min_val = min(tree.value, left_min_val, right_min_val)
    max_val = max(tree.value, left_max_val, right_max_val)

    return is_valid, min_val, max_val

#################################

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

def validateBst4(tree):
    """Check that tree is a valid binary search tree."""
    return _BSTValidator().validateBst(tree)

