# https://blog.csdn.net/will130/article/details/51187597

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        copy = num
        result = 0

        while True:
            digits = list()

            while copy >= 1:
                digits.append(copy % 10)
                copy = copy // 10

            for elem in digits:
                result += elem

            if result < 10:
                break

            copy = result
            result = 0

        return result
