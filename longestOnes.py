'''
思路：

用双指针lo, hi维护全部是1的区间，

用hi线性扫描，

如果碰到0， zero += 1

如果已经有k个zero了，说明区间左端应该向右调整到跨越过一个0的位置。

每次循环用res记录下当前的区间最大长度。
'''

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        zero = 0
        lo, hi = 0, 0
        res = 0

        for hi in range(len(A)):
            if A[hi] == 0:
                zero += 1

            while zero > K:
                if A[lo] == 0:
                    zero -= 1
                lo += 1

            # print lo, hi
            res = max(res, hi - lo + 1)

        return res
