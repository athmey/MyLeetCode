# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # 653.两数之和IV - 输入BST
        if root is None:
            return False

        # 这道题还是用BST的中序遍历，得到有序数组
        vals = self.inOrderTraverse(root)

        if len(vals) <= 1:
            return False

        low = 0
        high = len(vals) - 1

        while low < high:
            sum = vals[low] + vals[high]

            if sum == k:
                return True
            elif sum > k:
                high -= 1
            else:
                low += 1

        return False

    def inOrderTraverse(self, root):

        nodes = []
        node = root
        res = []

        while node is not None or len(nodes) > 0:
            if node is not None:
                nodes.append(node)
                node = node.left

            else:
                node = nodes.pop()
                res.append(node.val)

                node = node.right

        return res