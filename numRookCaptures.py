class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        cols = len(board[0])

        rock_row = 0
        rock_col = 0

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'R':
                    rock_row = i
                    rock_col = j
                    break

        res = 0

        # 向北
        for i in range(rock_row, rows):
            if board[i][rock_col] == 'p':
                res += 1
                break
            elif board[i][rock_col] == 'B':
                break

        # 向南
        for i in range(rock_row, -1, -1):
            if board[i][rock_col] == 'p':
                res += 1
                break
            elif board[i][rock_col] == 'B':
                break

        # 向东
        for j in range(rock_col, cols):
            if board[rock_row][j] == 'p':
                res += 1
                break
            elif board[rock_row][j] == 'B':
                break

        # 向西
        for j in range(rock_col, -1, -1):
            if board[rock_row][j] == 'p':
                res += 1
                break
            elif board[rock_row][j] == 'B':
                break

        return res