class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 36. 有效的数独
        # 9*9的格子

        if board is None:
            return False

        # 按行扫描
        for row in board:
            buff = []
            for j in range(len(row)):
                # 如果该字符是个数字
                if row[j] != '.':
                    num = int(row[j])

                    if num in buff:
                        return False
                    else:
                        buff.append(num)

        # 按列扫描
        for j in range(len(board[0])):
            buff = []
            for i in range(len(board)):
                # 如果该字符是个数字
                if board[i][j] != '.':
                    num = int(board[i][j])

                    if num in buff:
                        return False
                    else:
                        buff.append(num)

        # 按 3*3 九宫格扫描
        for m in range(0, 3):
            for n in range(0, 3):
                buff = []
                for i in range(3*m, 3*(m+1)):
                    for j in range(3*n, 3*(n+1)):
                        # 如果该字符是个数字
                        if board[i][j] != '.':
                            num = int(board[i][j])

                            if num in buff:
                                return False
                            else:
                                buff.append(num)

        return True



