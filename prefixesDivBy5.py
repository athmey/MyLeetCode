class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = list()

        if A is None or len(A) == 0:
            return result

        total_string = ''
        for digit in A:
            total_string = total_string + str(digit)

        for index in range(1, len(A)+1):
            current_string = total_string[:index]
            current_integer = int(current_string, 2)

            if current_integer % 5 == 0:
                result.append(True)

            else:
                result.append(False)

        return result