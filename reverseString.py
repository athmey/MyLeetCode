class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        if s is None or len(s) is 0:
            return

        else:
            for i in range(len(s)//2):
                tmp = s[i]
                s[i] = s[len(s) - i - 1]
                s[len(s) - i - 1] = tmp
            return