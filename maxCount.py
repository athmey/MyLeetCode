# 598. 范围求和 II

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        '''
        由于ops的每个操作a 的范围是 [1,m]，b 的范围是 [1,n], 则每次操作必定有数字会增加1, 则求这些操作的涉及的面积的交集就好了;

        所以求所以a的最小值, 和b的最小值, 得到的面积就是含有最大整数的元素个数
        '''
        if ops is None or len(ops) == 0:
            return m*n

        return min(i[0] for i in ops) * min(i[1] for i in ops)
