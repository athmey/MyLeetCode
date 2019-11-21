class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1:
            return 0

        copy = list(heights)

        copy.sort()

        res = 0
        for i in range(len(heights)):
            if copy[i] != heights[i]:
                res += 1

        return res
    