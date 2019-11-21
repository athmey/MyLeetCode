class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3 or A is None:
            return 0

        start = 0
        end = len(A) -1

        while start < end:
            if A[start] < A[start + 1]:
                start += 1

            if A[end] < A[end -1]:
                end -= 1

            if A[start] == A[end]:
                return start

        return 0