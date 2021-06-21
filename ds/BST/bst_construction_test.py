import unittest

from .bst_construction import BST_Iterative, BST_Recursive


class TestBST(unittest.TestCase):
    def test_case_1(self):
        root = BST_Iterative(10)
        root.left = BST_Iterative(5)
        root.left.left = BST_Iterative(2)
        root.left.left.left = BST_Iterative(1)
        root.left.right = BST_Iterative(5)
        root.right = BST_Iterative(15)
        root.right.left = BST_Iterative(13)
        root.right.left.right = BST_Iterative(14)
        root.right.right = BST_Iterative(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))


if __name__ == "__main__":
    unittest.main()
