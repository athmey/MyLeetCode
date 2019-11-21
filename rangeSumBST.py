# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        # 938. 二叉搜索树的范围和
        if root is None:
            return 0

        # 对BST进行中序遍历，得到排好序的数组：
        vals = self.inOrderTraverse(root)

        start_pos = vals.index(L)
        end_pos = vals.index(R)

        res = 0
        for i in range(start_pos, end_pos+1):
            res += vals[i]

        return res

    def inOrderTraverse(self, root):
        res = []

        if root is None:
            return res

        nodes = []
        node = root

        while node is not None or len(nodes) > 0:
            if node is not None:
                nodes.append(node)
                node = node.left

            else:
                node = nodes.pop()
                res.append(node.val)
                node = node.right

        return res
