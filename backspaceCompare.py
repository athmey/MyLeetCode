class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # 本题利用list 模拟栈 来模拟退格的操作
        stack_s = []
        stack_t = []

        for c in S:
            if len(stack_s) == 0:
                if c != '#':
                    stack_s.append(c)

            else:
                if c == '#':
                    stack_s.pop()

                else:
                    stack_s.append(c)

        for c in T:
            if len(stack_t) == 0:
                if c != '#':
                    stack_t.append(c)

            else:
                if c == '#':
                    stack_t.pop()

                else:
                    stack_t.append(c)

        return stack_s == stack_t