class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int

        hint:https://www.cnblogs.com/hutonm/p/5624996.html
        """
        result = 0

        while n >= 1:
            n = n // 5
            result += n

        return result