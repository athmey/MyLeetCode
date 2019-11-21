"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# 589. N叉树的前序遍历

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        nodes = []

        if root is None:
            return res

        nodes.append(root)

        while len(nodes) != 0:
            current_node = nodes.pop()

            if current_node is not None:
                res.append(current_node.val)

                for i in range(len(current_node.children)-1,-1,-1):
                    nodes.append(current_node.children[i])

        return res
