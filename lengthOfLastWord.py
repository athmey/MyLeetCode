class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0

        s = s.strip()
        if s is '':
            return 0

        lastword = s.split()[-1]
        return len(lastword)