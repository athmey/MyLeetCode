# 949. 给定数字能组成的最大时间
from itertools import permutations

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        if A is None or len(A) < 4:
            return ''

        self.res= []
        sublist = []

        # 先利用四个数字构建全排列
        self.getPermutations(A, sublist)
        print(len(self.res))
        print(self.res)

        global_max = -1
        result = ''
        for h1,h2,m1,m2 in self.res:
            hour = h1*10 + h2
            if hour >= 24:
                continue

            minute = m1*10 + m2
            if minute >= 60:
                continue

            if hour * 100 + minute > global_max:
                global_max = hour * 100 + minute
                result = '{}{}:{}{}'.format(h1,h2,m1,m2)

        return result

    def getPermutations(self, Nums, subList):
        # 结束条件
        if len(subList) == 4:
            self.res.append(subList[:])

        for i in range(len(Nums)):
            subList.append(Nums[i])

            copy = list(Nums)
            copy.remove(Nums[i])
            self.getPermutations(copy, subList)

            subList.pop()

if __name__ == '__main__':
    s = Solution()
    s.largestTimeFromDigits([0,4,0,3])
