class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 本题的核心就是26进制
        res = ''

        if n <= 0:
            return res

        copy = n

        while copy >= 1:
            copy -= 1

            remain = copy % 26


            res += chr(ord('A') + remain)

            copy //= 26

        return res[::-1]