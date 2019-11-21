class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cnt = 0
        for i in A:
            if i < 0:
                cnt += 1

        # 负数的个数比K大，那么把绝对值最大的K个负数翻过来即可
        if cnt >= K:
            A.sort()
            s = -1 * sum(A[:K]) + sum(A[K:])
            return s

        # 负数的个数比K小，那么把所有负数先翻过来，然后再去不停翻转绝对值最小的那个数
        else:
            temp = K - cnt
            B = list()

            for item in A:
                B.append(abs(item))
            # print B
            B.sort()
            # print sum(B), B
            if temp % 2 == 1:
                return sum(B) - 2 * B[0]
            else:
                return sum(B)