class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row_num = 1

        sum = 0

        while sum <= n:
            sum += row_num

            row_num += 1

        return row_num - 2