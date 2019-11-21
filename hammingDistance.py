class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        distance = 0

        if len(x_bin) < len(y_bin):
            while len(x_bin) < len(y_bin):
                x_bin = '0' + x_bin

        else:
            while len(y_bin) < len(x_bin):
                y_bin = '0' + y_bin

        print('X: ', x_bin)
        print('Y: ', y_bin)

        for index in range(len(x_bin)):
            if x_bin[index] != y_bin[index]:
                distance += 1

        return distance