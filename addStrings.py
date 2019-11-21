class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ''
        carry = 0

        counter = 1

        while counter <= min(len(num1), len(num2)):
            sum = int(num1[len(num1) - counter]) + int(num2[len(num2) - counter]) + carry

            carry = sum // 10

            sum = sum % 10

            counter += 1

            result += str(sum)

        if len(num1) > len(num2):
            while counter <= len(num1):
                sum = int(num1[len(num1) - counter]) + carry

                carry = sum // 10

                sum = sum % 10

                counter += 1

                result += str(sum)

        else:
            while counter <= len(num2):
                sum = int(num2[len(num2) - counter]) + carry

                carry = sum // 10

                sum = sum % 10

                counter += 1

                result += str(sum)

        if carry != 0:
            result += str(carry)

        return result[::-1]