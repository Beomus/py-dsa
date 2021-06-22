import unittest

from bst_validate import BST, validateBst


class TestValidation(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)

        self.assertTrue(validateBst(root))

    def test_case_2(self):
        root = BST(10)
        root.left = BST(10)
        root.right = BST(15)

        self.assertFalse(validateBst(root))

    def test_case_3(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(10)

        self.assertTrue(validateBst(root))

    def test_case_4(self):
        root = BST(10)
        root.left = BST(11)
        root.right = BST(9)

        self.assertFalse(validateBst(root))

    def test_case_5(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.right = BST(22)
        root.right.left.right = BST(16)

        self.assertFalse(validateBst(root))

    def test_case_6(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.right = BST(22)
        root.right.right.left = BST(16)

        self.assertTrue(validateBst(root))


if __name__ == "__main__":
    unittest.main()
