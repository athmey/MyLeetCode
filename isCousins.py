# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 993. 二叉树的堂兄弟节点

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution(object):
    def recursive(self,node,level,parent,x,y):
        if node.val == x:
            self.x_p = parent
            self.x_l = level
        elif node.val == y:
            self.y_p = parent
            self.y_l = level

        if node.left != None:
            self.recursive(node.left,level+1,node,x,y)
        if node.right != None:
            self.recursive(node.right, level + 1, node, x, y)

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.x_p = None
        self.y_p = None
        self.x_l = 0
        self.y_l = 0
        self.recursive(root, 0, None, x, y)
        return self.x_p != self.y_p and self.x_l == self.y_l
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 也可以采用层次遍历发方法来做这道题
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False

        current_level = []
        next_level = []

        current_level.append(root)

        while len(current_level) != 0:
            next_level_val = []

            for node in current_level:
                if node.left is not None:
                    next_level.append(node.left)
                    next_level_val.append(node.left.val)

                if node.right is not None:
                    next_level.append(node.right)
                    next_level_val.append(node.right.val)

            # 现在我们有了上下两层的所有节点，开始检查x,y是否为堂兄弟
            if x in next_level_val and y in next_level_val:
                # 检查他们是否为同一个父亲
                for node in current_level:
                    if node.left is not None and node.right is not None:
                        if node.left.val == x and node.right.val == y:
                            return False
                        elif node.left.val == y and node.right.val == x:
                            return False
                return True

            current_level = next_level
            next_level = []

        return False




