class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []

        if A is None or len(A) == 0:
            return res

        records = {}

        for index in range(len(A)):

            for c in A[index]:
                if c in records.keys():
                    records[c][index] += 1
                else:
                    records[c] = [0] * len(A)
                    records[c][index] = 1

        for key in records.keys():
            val = records[key]

            for i in range(min(val)):
                res.append(key)

        return res
