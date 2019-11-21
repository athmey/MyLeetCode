# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 872. 叶子相似的树
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        # 两棵树用同样的方式遍历，找出所有的叶子节点并比较
        leaf_vals1 = self.preOrderTraverse(root1)
        leaf_vals2 = self.preOrderTraverse(root2)

        return leaf_vals1 == leaf_vals2

    def preOrderTraverse(self, root):
        nodes = []

        leaf_vals = []
        nodes.append(root)

        while len(nodes) > 0:
            node = nodes.pop()

            if node.left is None and node.right is None:
                leaf_vals.append(node.val)

            if node.right is not None:
                nodes.append(node.right)

            if node.left is not None:
                nodes.append(node.left)

        return leaf_vals