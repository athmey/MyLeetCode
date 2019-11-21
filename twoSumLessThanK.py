class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if A is None and len(A) == 0:
            return -1

        list.sort(A)

        low = 0
        high = len(A) - 1

        min_diff = A[-1]

        while low < high:
            if A[low] + A[high] >= K:
                high -= 1

            else:
                diff = K - (A[low] + A[high])
                min_diff = min(diff, min_diff)
                low += 1

        return -1 if min_diff == A[-1] else K - min_diff
