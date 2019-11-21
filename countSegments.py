# 434. 字符串中的单词数

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        s = s.strip()

        words = s.split()

        return len(words)
