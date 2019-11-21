class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 557.反转字符串中的单词 III

        if s is None or len(s) == 0:
            return ''

        res = ''

        words = s.split()

        for word in words:
            res += word[::-1] + ' '

        return res[:-1]