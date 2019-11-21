class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s is None or t is None:
            return str()

        t_list = list(t)

        for c in s:
            if c in t_list:
                t_list.remove(c)

        return t_list[0]