class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 进位符号
        carry = 0
        counter = 1

        result = ''

        while counter <= min(len(a), len(b)):
            sum = int(a[len(a) - counter]) + int(b[len(b) - counter]) + carry

            carry = sum // 2
            sum = sum % 2

            result += str(sum)

            counter += 1

        if len(a) > len(b):
            while counter <= len(a):
                sum = int(a[len(a) - counter]) + carry

                carry = sum // 2
                sum = sum % 2

                result += str(sum)

                counter += 1

        else:
            while counter <= len(b):
                sum = int(b[len(b) - counter]) + carry

                carry = sum // 2
                sum = sum % 2

                result += str(sum)

                counter += 1

        if carry != 0:
            result += str(carry)

        return result[::-1]