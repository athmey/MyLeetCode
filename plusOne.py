class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) == 0:
            return digits

        carry = 0
        result = []

        first_time = True

        for index in range(len(digits)-1, -1, -1):
            if first_time:
                sum = digits[index] + 1 + carry
                first_time = False
            else:
                sum = digits[index] + carry

            carry = sum // 10
            sum %= 10

            result.insert(0, sum)

        if carry != 0:
            result.insert(0, carry)

        return result