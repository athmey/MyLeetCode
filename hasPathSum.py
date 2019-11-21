# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        path = []
        paths = []

        self.calculate_path_sum(root, paths, path, sum)

        if len(paths) >= 1:
            return True
        else:
            return False

    def calculate_path_sum(self, node, paths, path, sum):
        # 当前节点不为空
        if node is not None:
            path.append(node)

            # 当前节点是叶子节点
            if node.left is None and node.right is None:
                res = 0
                for node in path:
                    res += node.val

                if res == sum:
                    paths.append(list(path))
            else:
                if node.left:
                    self.calculate_path_sum(node.left, paths, path, sum)

                if node.right:
                    self.calculate_path_sum(node.right, paths, path, sum)

            path.pop()
