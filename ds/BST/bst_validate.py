class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return _validateBst(tree, float("-inf"), float("inf"))


def _validateBst(tree, minVal, maxVal):
    if tree is None:
        return True
    elif tree.value < minVal or tree.value >= maxVal:
        return False
    else:
        return _validateBst(tree.left, minVal, tree.value) and _validateBst(
            tree.right, tree.value, maxVal
        )
