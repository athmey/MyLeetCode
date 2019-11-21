class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None

        s = s.strip()

        if len(s) is 0:
            return ''
        if len(s) is 1:
            return s

        records = dict()

        for c in s:
            if c in records.keys():
                records[c] += 1
            else:
                records[c] = 1

        list1 = [(k,v) for k,v in zip(records.keys(),records.values())]
        list1_sort = sorted(list1, key=lambda x:x[1], reverse = True)

        result = ''
        for pair in list1_sort:
            for i in range(pair[1]):
                result = result + str(pair[0])

        return result
