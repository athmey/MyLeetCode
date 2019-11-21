# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return None

        paths = []
        path = []
        self.find_path(root, paths, path)

        result = []
        for path in paths:
            path_str = ''

            for node in path:
                path_str += str(node.val)
                path_str += '->'
            path_str = path_str[:-2]
            result.append(path_str)

        return result

    def find_path(self, node, paths, path):
        if node is not None:
            # node is leaf
            if node.left is None and node.right is None:
                path.append(node)

                tmp = list(path)
                paths.append(tmp)

            else:
                path.append(node)

                if node.left:
                    self.find_path(node.left, paths, path)

                if node.right:
                    self.find_path(node.right, paths, path)

            # 还原现场，将当前node弹出path
            path.pop()