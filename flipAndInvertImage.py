class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 832. 翻转图像
        # 根据题意，每一张图像都是正方形

        res = []

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    A[i][j] = 1

                else:
                    A[i][j] = 0

            res.append(A[i][::-1])

        return res