# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1022. 从根到叶的二进制数之和
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.paths = []
        path = []

        self.getPath(root, path)
        sum = 0

        for path in self.paths:
            vals = ''
            for node in path:
                vals += str(node.val)

            sum += int(vals, 2)

        return sum

    def getPath(self, root, path):
        if root is not None:
            # 如果当前节点是叶子节点
            if root.left is None and root.right is None:
                path.append(root)
                temp = list(path)
                self.paths.append(temp)

            else:
                path.append(root)

                if root.left is not None:
                    self.getPath(root.left, path)

                if root.right is not None:
                    self.getPath(root.right, path)

            # 恢复现场，将当前节点弹出
            path.pop()




