# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.isUniversal(root)

    def isUniversal(self, root):
        if root is None:
            return True

        elif root.left is None and root.right is None:
            return True

        elif root.left is None and root.right is not None:
            if root.val == root.right.val:
                return self.isUniversal(root.right)
            else:
                return False

        elif root.left is not None and root.right is None:
            if root.val == root.left.val:
                return self.isUniversal(root.left)
            else:
                return False

        else:
            if root.val == root.left.val and root.val == root.right.val:
                return self.isUniversal(root.left) and self.isUniversal(root.right)
            else:
                return False
