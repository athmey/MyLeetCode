class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x

        n = abs(n)
        x0 = x * x
        return self.myPow(x0, n // 2) if (n % 2 == 0) else x * self.myPow(x0, n // 2)
