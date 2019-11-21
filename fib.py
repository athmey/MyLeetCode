class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        if N is 0:
            return 0

        if N is 1:
            return 1

        result = list()
        result.append(int(0))
        result.append(int(1))

        for i in range(2, N+1):
            cur = result[0] + result[1]
            result.pop(0)
            result.append(cur)

        return result[-1]
