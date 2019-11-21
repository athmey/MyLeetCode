# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        else:
            leftLeaves_values = list()
            self.get_all_leftLeaves_values(root, leftLeaves_values)

            sum = 0
            for value in leftLeaves_values:
                sum += value
            return sum

    def isLeaf(self, node):
        if node is not None and node.left is None and node.right is None:
            return True
        else:
            return False

    def get_all_leftLeaves_values(self, root, leftLeaves_values):
        current_node = root
        nodes = list()
        nodes.append(current_node)

        while len(nodes) != 0:
            # code block for operations for root
            if self.isLeaf(current_node.left):
                leftLeaves_values.append(current_node.left.val)

            # operation for the subtree nodes
            if current_node.right is not None:
                nodes.append(current_node.right)

            if current_node.left is not None:
                nodes.append(current_node.left)

            current_node = nodes.pop()




