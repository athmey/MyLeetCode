# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

'''
-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
'''

# 374. 猜数字大小
# 看上去是一道典型的二分法

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessNum(0, n)

    def guessNum(self, low, high):
        mid = low + (high - low)//2

        if guess(mid) == 0:
            return mid

        elif guess(mid) == 1:
            return self.guessNum(mid+1, high)

        elif guess(mid) == -1:
            return self.guessNum(low, mid -1)



