class Solution:
    def mySqrt(self, n):
        if n == 0: return 0
        x0, x1 = float('inf'), n / 2.
        while abs(x0 - x1) > 1E-6:
            x0 = x1
            x1 = (x0 + n / x0) / 2.
        return int(x0)