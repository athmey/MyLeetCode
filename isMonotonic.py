# 896. 单调数列

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if A is None:
            return False

        if len(A) <= 2:
            return True

        # 先找到第一个不等号
        index = 0

        while index < len(A)-1:
            if A[index] != A[index+1]:
                break
            index += 1
        # 整个数列所有元素相等
        if index == len(A) -1:
            return True

        # 递减数列
        if A[index] > A[index+1]:
            for i in range(0, len(A)-1):
                if A[i] >= A[i+1]:
                    pass
                else:
                    return False
        # 递增数列
        else:
            for i in range(0, len(A)-1):
                if A[i] <= A[i+1]:
                    pass
                else:
                    return False
        return True



    '''

        temp1 = list(A)
        temp2 = list(A)

        list.sort(temp1)
        list.sort(temp2, reverse=True)

        return A == temp1 or A == temp2
    '''