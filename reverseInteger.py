class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isMinus = False
        if x < 0:
            isMinus = True

        upperRange = pow(2, 31)

        abs_x = abs(x)
        # get the every digit of x reversely
        digits_of_x = list()
        while abs_x >= 1:
            digit = int(abs_x % 10)
            digits_of_x.append(digit)

            abs_x = int(abs_x / 10)

        sum = 0
        power = len(digits_of_x) - 1
        for digit in digits_of_x:

            sum += digit * pow(10, power)
            power -= 1

        if isMinus:
            sum = sum * -1

        if sum >= upperRange - 1 or sum < upperRange * (-1):
            return 0
        else:
            return sum


