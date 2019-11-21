# 661. 图片平滑器

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        copy = [[0 for j in range(len(M[0]))] for i in range(len(M))]

        for i in range(len(M)):
            for j in range(len(M[0])):
                new_val = self.smooth(M, i, j)
                copy[i][j] = new_val

        return copy

    def smooth(self, M, i, j):
        count = 0
        total_sum = 0

        # 左上
        if i - 1 >= 0 and j - 1 >= 0:
            count += 1
            total_sum += M[i-1][j-1]

        # 上
        if i - 1 >= 0:
            count += 1
            total_sum += M[i-1][j]

        # 右上
        if i - 1 >= 0 and j + 1 < len(M[0]):
            count += 1
            total_sum += M[i-1][j+1]

        # 左
        if j - 1 >= 0:
            count += 1
            total_sum += M[i][j-1]

        # 右
        if j + 1 < len(M[0]):
            count += 1
            total_sum += M[i][j+1]

        # 左下
        if i + 1 < len(M) and j - 1 >= 0:
            count += 1
            total_sum += M[i+1][j-1]

        # 下
        if i + 1 < len(M):
            count += 1
            total_sum += M[i+1][j]

        # 右下
        if i + 1 < len(M) and j + 1 < len(M[0]):
            count += 1
            total_sum += M[i+1][j+1]

        total_sum += M[i][j]

        # print(i, j, total_sum)
        return total_sum // (count+1)

if __name__ == '__main__':
    s = Solution()

    l = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    s.imageSmoother(l)