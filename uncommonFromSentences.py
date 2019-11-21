class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dict_A = {}
        dict_B = {}

        result = []

        for word in A.strip().split():
            if word in dict_A.keys():
                dict_A[word] += 1

            else:
                dict_A[word] = 1

        for word in B.strip().split():
            if word in dict_B.keys():
                dict_B[word] += 1

            else:
                dict_B[word] = 1

        for key in dict_A.keys():
            if dict_A[key] == 1 and key not in dict_B.keys():
                result.append(key)

        for key in dict_B.keys():
            if dict_B[key] == 1 and key not in dict_A.keys():
                result.append(key)

        return result