# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None

        vals = self.preorderTraversal(root)

        # 将结果降序排列
        res = list(set(vals))
        list.sort(res)

        return -1 if len(res) == 1 else res[1]


    def preorderTraversal(self, root):
        if root is None:
            return root

       # using list to implemet stack
        else:
            res = []
            treeNodes = []
            treeNodes.append(root)

            # 只要列表不为空
            while len(treeNodes) > 0:
                # 现将当前自身节点放入结果中
                currentNode = treeNodes.pop()
                res.append(currentNode.val)

                if currentNode.right is not None:
                    treeNodes.append(currentNode.right)

                if currentNode.left is not None:
                    treeNodes.append(currentNode.left)

            return res
