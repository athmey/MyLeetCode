# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 897. 递增顺序查找树
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        vals = self.inOrderTraverse(root)

        # 根据节点值创建树
        root = TreeNode(vals[0])
        node = root
        node.left = None

        for i in range(1, len(vals)):
            node.right = TreeNode(vals[i])

            node = node.right
            node.left = None

        return root

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