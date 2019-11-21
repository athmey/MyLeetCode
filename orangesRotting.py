# 994. 腐烂的橘子

'''
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
'''


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        return self.rotting(grid, 0)

    def rotting(self, grid, minute):
        rot_positions = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果当前橘子是腐烂的橘子，将其周围的橘子全部腐烂
                if grid[i][j] == 2:
                    # 向上
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        # grid[i][j-1] = 2
                        pos = [i - 1, j]
                        rot_positions.append(pos)

                    # 向下
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        # grid[i][j+1] = 2
                        pos = [i + 1, j]
                        rot_positions.append(pos)

                    # 向左
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        # grid[i-1][j] = 2
                        pos = [i, j - 1]
                        rot_positions.append(pos)

                    # 向右
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        # grid[i+1][j] = 2
                        pos = [i, j + 1]
                        rot_positions.append(pos)

        # 当棋盘状态无法改变时，代表橘子腐烂光了或者状态无法继续了
        # 扫描棋盘，如果有未腐烂的橘子，代表状态无法继续；否则就是腐烂完毕
        if len(rot_positions) == 0:
            for row in grid:
                for orange in row:
                    if orange == 1:
                        return -1

            return minute
        else:
            for pos in rot_positions:
                grid[pos[0]][pos[1]] = 2

            return self.rotting(grid, minute + 1)

