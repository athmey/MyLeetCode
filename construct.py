"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

'''
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if grid is None:
            return None

        # 结束条件：当前节点是一个叶子节点
        if len(grid) == 1 and len(grid[0]) == 1:
            current_node = Node(grid[0][0], True, None, None, None, None)
            return current_node
        else:
            # 否则将当前网格继续划分，并构造当前网格对应的节点
            # 题目保证了grid 的尺寸是2的整数次幂,所以可以放心的不断除2
            new_grid_row_num = len(grid) // 2
            new_grid_col_num = len(grid[0]) // 2

            # 将当前网格切割成四个部分
            topLeft = []
            for i in range(new_grid_row_num):
                temp = []
                for j in range(new_grid_col_num):
                    temp.append(grid[i][j])
                topLeft.append(temp)

            topRight = []
            for i in range(new_grid_row_num):
                temp = []
                for j in range(new_grid_col_num, len(grid)):
                    temp.append(grid[i][j])
                topRight.append(temp)

            bottomLeft = []
            for i in range(new_grid_row_num, len(grid)):
                temp = []
                for j in range(new_grid_col_num):
                    temp.append(grid[i][j])
                bottomLeft.append(temp)

            bottomRight = []
            for i in range(new_grid_row_num, len(grid)):
                temp = []
                for j in range(new_grid_col_num, len(grid)):
                    temp.append(grid[i][j])
                bottomRight.append(temp)

            return Node(1, False, self.construct(topLeft), self.construct(topRight), self.construct(bottomLeft), self.construct(bottomRight))
'''
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return None
        if self.is_leaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        n = len(grid)
        return Node("*", False, self.construct([row[:n // 2] for row in grid[:n // 2]]),
                    self.construct([row[n // 2:] for row in grid[:n // 2]]),
                    self.construct([row[:n // 2] for row in grid[n // 2:]]),
                    self.construct([row[n // 2:] for row in grid[n // 2:]])
                    )

    def is_leaf(self, grid):
        # print(grid)
        vals = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                vals.add(grid[i][j])
                if len(vals) > 1:
                    return False
        return True
