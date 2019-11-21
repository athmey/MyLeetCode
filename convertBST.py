# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 538. 把二叉搜索树转换为累加树
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        # 先中序遍历
        vals = self.inOrderTraverse(root)

        # 再先序遍历改变每个节点的值
        return self.preOrderTraverse(root, vals)


    def inOrderTraverse(self, root):
        if root is None:
            return root

        node = root
        nodes = []
        vals = []

        while node is not None or len(nodes) != 0:
            if node is not None:
                nodes.append(node)
                node = node.left

            else:
                node = nodes.pop()
                vals.append(node.val)
                node = node.right

        return vals

    def preOrderTraverse(self, root, vals):
        if root is None:
            return root

        if vals is None or len(vals) == 0:
            return root

        nodes = []
        nodes.append(root)

        while len(nodes) != 0:
            node = nodes.pop()
            val = node.val

            index = vals.index(val)

            local_sum = sum(vals[index+1:])

            node.val = val + local_sum

            if node.right is not None:
                nodes.append(node.right)

            if node.left is not None:
                nodes.append(node.left)

        return root




'''
class Solution:
     def convertBST(self, root):
         # 递归算法 分析：先遍历右节点，再存储根节点，最后遍历左节点
         self.sum = 0
         def dfs(root):
             if not root: 
                return root
                
             dfs(root.right)
             
             self.sum = self.sum + root.val
             root.val = self.sum
             dfs(root.left)
             return root
         return dfs(root)
         
         
class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        # 非递归算法
        def dfs(root):
            if not root: return root
            stack = []
            node = root
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.right
                node = stack.pop()
                self.sum += node.val
                node.val = self.sum
                self.sum = node.val
                node = node.left
            return root
        return dfs(root)

'''