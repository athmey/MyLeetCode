# 1078. Bigram 分词

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []

        if text is None or len(text) <= 2:
            return res

        temp = text.split()

        for i in range(2, len(temp)):
            if temp[i-1] == second and temp[i-2] == first:
                res.append(temp[i])

        return res