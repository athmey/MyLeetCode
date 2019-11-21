class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None or len(A) is 0:
            return 0

        threshold = len(A) //2
        counter = 1
        A.sort()

        for index in range(1,len(A)):
            if A[index] == A[index - 1]:
                counter += 1

                if counter == threshold:
                    return A[index]

            else:
                counter = 1

        return 0