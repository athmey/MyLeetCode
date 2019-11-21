# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 102. 二叉树的层次遍历
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res

        current_level = []
        next_level = []

        current_level.append(root)

        while len(current_level) != 0:
            current_level_val = []

            for node in current_level:
                current_level_val.append(node.val)

                if node.left is not None:
                    next_level.append(node.left)

                if node.right is not None:
                    next_level.append(node.right)

            res.append(current_level_val)
            current_level = next_level
            next_level = []

        return res
