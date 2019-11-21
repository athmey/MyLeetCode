class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False

        if c == 0 or c == 1 or c == 2:
            return True

        for num1 in range(0, int(c**0.5) + 1):
            num2 = c - num1 * num1

            if self.isPerfectSquare(num2):
                return True

        return False

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num**0.5 - int(num**0.5) == 0