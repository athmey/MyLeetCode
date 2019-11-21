# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 637. 二叉树的层平均值

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level_order_averages = []

        level_order_vals = self.levelOrderTraverse(root)

        for level_order_val in level_order_vals:
            tmp = float(sum(level_order_val)) / len(level_order_val)
            level_order_averages.append(tmp)

        return level_order_averages


    def levelOrderTraverse(self, root):
        result = []

        if root is None:
            return result

        current_level = []
        next_level = []

        current_level.append(root)

        while len(current_level) != 0:
            current_level_vals = []

            for node in current_level:
                current_level_vals.append(node.val)

                if node.left is not None:
                    next_level.append(node.left)

                if node.right is not None:
                    next_level.append(node.right)

            result.append(current_level_vals)
            current_level = next_level
            next_level = []

        return result