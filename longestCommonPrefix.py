class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) is 0:
            return ''

        elif len(strs) is 1:
            return strs[0]

        else:
            # get the shortest word length in list
            shortest_length = len(strs[0])
            for str in strs[1:]:
                if len(str) < shortest_length:
                    shortest_length = len(str)

            # traverse the word to get the result
            result = ''
            for i in range(shortest_length):
                for index in range(1, len(strs)):
                    if strs[index][i] != strs[index-1][i]:
                        return result
                # append the current char to result
                result += strs[0][i]

            return result