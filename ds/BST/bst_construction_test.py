import unittest

from bst_construction import BST_Iterative, BST_Recursive


class TestBST(unittest.TestCase):
    def setUp(self) -> None:
        self.BST = [BST_Iterative, BST_Recursive]

    def test_case_1(self):
        for BST in self.BST:
            root = BST(10)
            root.left = BST(5)
            root.left.left = BST(2)
            root.left.left.left = BST(1)
            root.left.right = BST(5)
            root.right = BST(15)
            root.right.left = BST(13)
            root.right.left.right = BST(14)
            root.right.right = BST(22)

            root.insert(12)
            self.assertTrue(root.right.left.left.value == 12)

            root.remove(10)
            self.assertTrue(not root.contains(10))
            self.assertTrue(root.value == 12)

            self.assertTrue(root.contains(15))

    def test_case_2(self):
        for BST in self.BST:
            root = BST(10)
            root.insert(5)
            root.insert(15)
            self.assertTrue(root.right.value == 15)
            self.assertTrue(root.left.value == 5)

            root.remove(5)
            root.remove(15)
            self.assertTrue(not root.contains(5))
            self.assertTrue(not root.contains(15))

            root.remove(10)
            self.assertTrue(root.contains(10))
            self.assertEqual(root.value, 10)

    def test_case_3(self):
        for BST in self.BST:
            root = BST(10)
            root.insert(5)
            root.insert(15)

            self.assertFalse(root.contains(1))
            self.assertFalse(root.contains(6))
            self.assertFalse(root.contains(11))

            self.assertTrue(root.contains(10))
            self.assertTrue(root.contains(15))
            self.assertTrue(root.contains(5))

    def test_case_4(self):
        for BST in self.BST:
            root = BST(1)
            root.insert(2)
            root.insert(3)
            root.insert(4)

            root.remove(1)
            self.assertFalse(root.contains(1))
            self.assertEqual(root.value, 2)

            root.insert(1)
            self.assertEqual(root.left.value, 1)

            root.remove(2)
            self.assertEqual(root.value, 3)

    def test_case_5(self):
        for BST in self.BST:
            root = BST(1)
            root.insert(-1)
            root.insert(-3)
            root.insert(-2)

            self.assertEqual(root.left.value, -1)
            self.assertEqual(root.left.left.value, -3)
            self.assertEqual(root.left.left.right.value, -2)

            root.remove(-1)
            self.assertEqual(root.left.value, -3)
            self.assertTrue(root.contains(-2))


if __name__ == "__main__":
    unittest.main()
