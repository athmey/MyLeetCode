# 953. 验证外星语词典

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # order是按升序排列的
        self.order = order
        copy = list(words)
        list.sort(copy, cmp = self.compare)

        return copy == words


    def compare(self, s1, s2):
        # 1:s1>s2
        # 0:s1==s2
        #-1:s1<s2

        buffer = list(self.order)

        table = {}

        for index, val in enumerate(buffer):
            if val not in table.keys():
                table[val] = index

        # 开始比较字符串s1，s2
        # 先比较公共长度的部分
        for i in range(min(len(s1), len(s2))):
            if table[s1[i]] > table[s2[i]]:
                return 1
            elif table[s1[i]] < table[s2[i]]:
                return -1

        if len(s1) == len(s2):
            return 0
        elif len(s1) > len(s2):
            return 1
        else:
            return -1


