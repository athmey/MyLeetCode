# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        left_subtree_height = self.get_tree_height(root.left)
        right_subtree_height = self.get_tree_height(root.right)

        if abs(left_subtree_height - right_subtree_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def get_tree_height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.get_tree_height(root.left), self.get_tree_height(root.right))
