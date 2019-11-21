# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        if root is None:
            return 0

        tree_node_values = self.inorderTraversal(root)
        min_diff = sys.maxsize

        for index in range(len(tree_node_values) - 1):
            if min_diff > tree_node_values[index + 1] - tree_node_values[index]:
                min_diff = tree_node_values[index + 1] - tree_node_values[index]

        return min_diff


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        treeNodes = []

        if root is None:
            return res

        else:
            currentNode = root

            while currentNode is not None or len(treeNodes) > 0:
                # if current node is not none,push left subtree into the queue first
                if currentNode is not None:
                    treeNodes.append(currentNode)
                    currentNode = currentNode.left

                else:
                    currentNode = treeNodes.pop()
                    res.append(currentNode.val)
                    currentNode = currentNode.right

            return res

