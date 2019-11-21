class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A is None:
            return None

        if len(A) is 0:
            return list()

        result = list()

        for num in A:
            result.append(num**2)

        result.sort()
        return result