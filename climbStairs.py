class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 走法符合斐波那契数列的规律

        if n is 0 or n is 1:
            return 1

        else:
            a = 1
            b = 1
            sum = 0
            for i in range(2, n+1):
                #print('i: ',i)
                sum = a + b
                a = b
                b = sum

            return sum
