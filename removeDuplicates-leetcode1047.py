class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 1:
            return S

        copy = S

        # 用一个链表模拟字符碰撞的过程
        buff = []

        for c in copy:
            if len(buff) == 0:
                buff.append(c)

            else:
                if c == buff[-1]:
                    buff.pop()

                else:
                    buff.append(c)

        res = ''
        for c in buff:
            res += c

        return res