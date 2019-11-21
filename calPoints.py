class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        if ops is None or len(ops) == 0:
            return 0

        result = 0

        number_list = []
        for op in ops:
            if op.isnumeric() or op[1:].isnumeric():
                result += int(op)

                number_list.append(int(op))

            elif op == 'C':
                item = number_list.pop()
                result -= item

            elif op == 'D':
                result += 2 * number_list[-1]
                number_list.append(2 * number_list[-1])

            elif op == '+':
                current_num = number_list[-2] + number_list[-1]
                number_list.append(current_num)
                result += current_num

        return result







