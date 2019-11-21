import sys

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # 判断B中是否存在A中没有的字母，如果存在直接返回False
        char_in_A = set(A)
        for c in B:
            if c not in char_in_A:
                return -1

        # 因为一个完整的B可能首部用到A的一部分，尾部用到A的一部分，像这样A'[AA....AA]A' , [ ] 内必然<=B的长度，故总长<=2*A+B
        maxlen = len(A + A + B)
        a = A
        counter = 1

        while len(a) <= maxlen:
            if -1 != a.find(B):
                return counter

            counter += 1
            a = a + A

        return -1

