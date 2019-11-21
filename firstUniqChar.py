class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return -1

        s = s.strip()

        if len(s) is 0:
            return -1
        if len(s) is 1:
            return 0

        records = dict()

        for c in s:
            if c in records.keys():
                records[c] += 1
            else:
                records[c] = 1

        global_min_index = len(s);
        for key,val in records.items():
            if val is 1:
                if s.index(key) < global_min_index:
                    global_min_index = s.index(key)

        if global_min_index == len(s):
            return -1
        else:
            return global_min_index
