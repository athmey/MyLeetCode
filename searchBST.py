# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        # 用二叉树的先序遍历直接做
        return self.preOrderTraverse(root, val)

    def preOrderTraverse(self, root, val):

        nodes = []

        nodes.append(root)

        while len(nodes) > 0:
            node = nodes.pop()

            if node.val == val:
                return node

            else:
                if node.right is not None:
                    nodes.append(node.right)

                if node.left is not None:
                    nodes.append(node.left)

        return None
