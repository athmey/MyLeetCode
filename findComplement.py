class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_bin = bin(num)[2:]

        complement_bin = str()

        for c in num_bin:
            if c == '1':
                complement_bin = complement_bin + '0'
            else:
                complement_bin = complement_bin + '1'

        print(complement_bin)
        return int(complement_bin,2)
