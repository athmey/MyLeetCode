# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 783. 二叉搜索树结点最小距离
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # 中序遍历BST，将所有元素按升序拍好
        vals = self.inOrderTraverse(root)

        diffs = []

        for i in range(1, len(vals)):
            diffs.append(vals[i]-vals[i-1])

        return min(diffs)

    def inOrderTraverse(self, root):
        if root is None:
            return []

        vals = []
        nodes = []
        node = root

        while node is not None or len(nodes) > 0:
            if node is not None:
                nodes.append(node)
                node = node.left

            else:
                node = nodes.pop()

                # 处理当前左节点
                vals.append(node.val)

                node = node.right

        return vals

