"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# 559. N叉树的最大深度

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0

        else:
            max_depth_of_children = 0

            for child in root.children:
                max_depth_of_current_child = self.maxDepth(child)

                if max_depth_of_children < max_depth_of_current_child:
                    max_depth_of_children = max_depth_of_current_child

            return 1 + max_depth_of_children

