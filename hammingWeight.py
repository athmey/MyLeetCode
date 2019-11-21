class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = bin(n)[2:]

        return bin_n.count('1')