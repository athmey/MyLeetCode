class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if S is None or len(S) == 0:
            return 0

        res = 0
        for c in S:
            if c in J:
                res += 1

        return res
    