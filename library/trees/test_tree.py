import unittest
from tree_node import (
    TreeNode,
    BinaryTreeNode,
    inorder_traversal,
    postorder_traversal,
    preorder_traversal,
    eulerian_tour
)

class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        # Binary Tree:
        #       1
        #     /   \
        #    2     3
        #   / \   / \
        #  4   5 6   7
        self.binary_tree = BinaryTreeNode(1,
            BinaryTreeNode(2,
                BinaryTreeNode(4),
                BinaryTreeNode(5)
            ),
            BinaryTreeNode(3,
                BinaryTreeNode(6),
                BinaryTreeNode(7)
            )
        )

        # General Tree:
        #       1
        #    /  |  \
        #   2   3   4
        #  / \     / \
        # 5   6   7   8
        self.general_tree = TreeNode(1, [
            TreeNode(2, [
                TreeNode(5),
                TreeNode(6)
            ]),
            TreeNode(3),
            TreeNode(4, [
                TreeNode(7),
                TreeNode(8)
            ])
        ])

        # Single node binary tree
        self.single_node_binary = BinaryTreeNode(1)

        # Single node general tree
        self.single_node_general = TreeNode(1)

        # Binary tree with only left children
        self.left_skewed_binary = BinaryTreeNode(1,
            BinaryTreeNode(2,
                BinaryTreeNode(3)
            )
        )

        # Binary tree with only right children
        self.right_skewed_binary = BinaryTreeNode(1,
            None,
            BinaryTreeNode(2,
                None,
                BinaryTreeNode(3)
            )
        )

    def test_inorder_traversal(self):
        self.assertEqual(inorder_traversal(self.binary_tree), [4, 2, 5, 1, 6, 3, 7])

    def test_postorder_traversal(self):
        self.assertEqual(postorder_traversal(self.binary_tree), [4, 5, 2, 6, 7, 3, 1])

    def test_preorder_traversal(self):
        self.assertEqual(preorder_traversal(self.binary_tree), [1, 2, 4, 5, 3, 6, 7])

    def test_eulerian_tour(self):
        self.assertEqual(eulerian_tour(self.general_tree), [1, 2, 5, 5, 6, 6, 2, 3, 3, 4, 7, 7, 8, 8, 4, 1])

    def test_empty_tree(self):
        self.assertEqual(inorder_traversal(None), [])
        self.assertEqual(postorder_traversal(None), [])
        self.assertEqual(preorder_traversal(None), [])
        self.assertEqual(eulerian_tour(None), [])

    def test_single_node_binary(self):
        self.assertEqual(inorder_traversal(self.single_node_binary), [1])
        self.assertEqual(postorder_traversal(self.single_node_binary), [1])
        self.assertEqual(preorder_traversal(self.single_node_binary), [1])

    def test_single_node_general(self):
        self.assertEqual(eulerian_tour(self.single_node_general), [1, 1])

    def test_left_skewed_binary(self):
        self.assertEqual(inorder_traversal(self.left_skewed_binary), [3, 2, 1])
        self.assertEqual(postorder_traversal(self.left_skewed_binary), [3, 2, 1])
        self.assertEqual(preorder_traversal(self.left_skewed_binary), [1, 2, 3])

    def test_right_skewed_binary(self):
        self.assertEqual(inorder_traversal(self.right_skewed_binary), [1, 2, 3])
        self.assertEqual(postorder_traversal(self.right_skewed_binary), [3, 2, 1])
        self.assertEqual(preorder_traversal(self.right_skewed_binary), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
