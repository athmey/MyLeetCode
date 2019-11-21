class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True

        while num > 1:
            if num % 4 == 0:
                num = num // 4

            else:
                return False

        return True