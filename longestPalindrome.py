class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        count = 0

        chars = []
        for c in s:
            chars.append(c)

        # 找到s中所有能够配对的字母
        for c in s:
            if chars.count(c) >= 2:
                chars.remove(c)
                chars.remove(c)

                count += 2

        # 如果到最后还有字母能用，加上该字符成为回文字符串的中心
        if len(chars) >= 1:
            count += 1

        return count