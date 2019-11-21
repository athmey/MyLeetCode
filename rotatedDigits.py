# 788. 旋转数字
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 只有2，5，6，9构成的数字才是好数字
        counter = 0

        def isGoodNumber(n):
            badNum = ['3','4','7']
            goodNumber = [2,5,6,9]

            # 含有3，4，7的数字全部排除
            for c in str(n):
                if c in badNum:
                    return False

            # 剩下的这部分数字只含有0，1，8；2，5，6，9
            # 排除掉只含有0，1，8的数字
            buffer= list(set(list(str(n))))
            list.sort(buffer)

            for digit in buffer:
                if int(digit) in goodNumber:
                    return True

            return False


        for i in range(N+1):
            if isGoodNumber(i):
                counter += 1

        return counter

