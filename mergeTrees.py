# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 617. 合并二叉树
        if t1 is None:
            return t2

        if t2 is None:
            return t1

        return self.merge(t1, t2)

    def merge(self, n1, n2):
        # 如果传进来的两个点都不为空
        if n1 is not None and n2 is not None:
            new_node = TreeNode(n1.val + n2.val)

            new_node.left = self.merge(n1.left, n2.left)
            new_node.right = self.merge(n1.right, n2.right)

            return new_node

        elif n1 is not None and n2 is None:
            return n1

        elif n1 is None and n2 is not None:
            return n2
        # 两个节点都是空
        else:
            return None