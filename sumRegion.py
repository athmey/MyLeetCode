class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) is 0:
            return
        if len(matrix[0]) is 0:
            return

        self.__myRegion = matrix
        self.__rows = len(matrix)
        self.__cols = len(matrix[0])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        result = 0

        for i in range(row1, row2 +1):
            for j in range(col1, col2 +1):
                result += self.__myRegion[i][j]

        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)