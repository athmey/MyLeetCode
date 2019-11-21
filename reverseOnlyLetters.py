# 917. 仅仅反转字母
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S is None or len(S) <= 1:
            return S

        letters = []
        symbol_postions = []
        for i in range(len(S)):
            if S[i].isalpha():
                letters.append(S[i])

            else:
                symbol_postions.append(i)

        letters = letters[::-1]

        res = ''
        index = 0

        while index < len(S):
            if index in symbol_postions:
                res += S[index]

            else:
                res += letters[0]
                letters.pop(0)

            index += 1

        return res