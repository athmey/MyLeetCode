# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        else:
            values = list()
            self.inOrderTraversal(root, values)

            counter = {}
            for elem in values:
                if elem in counter.keys():
                    counter[elem] += 1
                else:
                    counter[elem] = 1

            pairs = sorted(counter.items(), key = lambda x: x[1], reverse=True)
            res = [k for k,v in pairs if v == pairs[-1][1]]

            return res

    def inOrderTraversal(self, root, res):
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
