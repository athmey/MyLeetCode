# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None:
            return None

        # 思路：
        # 注意题目中有说这是一个BST。那么满足左子树所有节点<根节点<右子树所有节点。
        # 假设p.val < q.val，那么它们的最近公共祖先节点r，一定满足：p.val <= r.val <=q.val。

        minn = min(p.val, q.val)
        maxn = max(p.val, q.val)

        if minn <= root.val <= maxn:
            return root
        else:
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)

            if l:
                return l
            if r:
                return r
