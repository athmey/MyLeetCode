class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for c in s:
            if c not in dict_s.keys():
                dict_s[c] = 1

            else:
                dict_s[c] += 1

        for c in t:
            if c not in dict_t.keys():
                dict_t[c] = 1

            else:
                dict_t[c] += 1

        for key in dict_s.keys():
            if key not in dict_t.keys():
                return False
            if dict_s[key] != dict_t[key]:
                return False

        return True