class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        if n is 1 or n is 2 or n is 3:
            return True

        else:
            return not (self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3))
        '''
        # n能被4整除则必输无疑
        return not(n % 4 is 0)