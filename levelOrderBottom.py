# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else:
            current_level = []
            next_level = []

            level_order = []

            current_level.append(root)

            while len(current_level) != 0:
                level_order.append(current_level)

                for node in current_level:
                    current_node = node

                    left_child_node = current_node.left
                    if left_child_node:
                        next_level.append(left_child_node)

                    right_child_node = current_node.right
                    if right_child_node:
                        next_level.append(right_child_node)

                current_level = next_level
                next_level = []

            level_order_val = []
            for level in level_order:
                tmp = []

                for node in level:
                    tmp.append(node.val)

                level_order_val.append(tmp)

            level_order_val_bottom = []
            for i in range(len(level_order_val)-1 ,-1,-1):
                level_order_val_bottom.append(level_order_val[i])

            return level_order_val_bottom

