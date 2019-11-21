class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if A is None or len(A) < 3:
            return False

        start = 1

        peak = 0

        while start <= len(A) -1:
            if A[start] > A[start - 1]:
                start +=1
            else:
                peak = start - 1
                break

        if peak == len(A) -1 or peak == 0:
            return False

        end = peak + 1


        while end < len(A):
            if A[end] < A[end -1]:
                end +=1
            else:
                return False

        return True
