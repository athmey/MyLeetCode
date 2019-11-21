# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, left, right):
        if left is None and right is None:
            return True

        if left is None and right is not None:
            return False

        elif left is not None and right is None:
            return False

        elif left.val != right.val:
            return False

        else:
            return self.isSymmetricTree(left.left, right.right) and self.isSymmetricTree(left.right, right.left)


