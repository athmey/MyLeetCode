class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        sum = 1

        for i in range(2, int(num ** 0.5) + 1 + 1):
            if num % i == 0:
                sum += (i + num //i)

            if i * i == num:
                sum -= i

            if sum > num:
                return False

        return sum == num

