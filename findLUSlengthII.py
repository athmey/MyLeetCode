# 522. 最长特殊序列 II

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # 找出列表中和别的所有字符串都不一样的最长字符串
        if strs is None or len(strs) == 0:
            return 0

        frequency_table = {}
        unique = []
        # 直接建一个字典存储出现频次信息
        for str in strs:
            if str in frequency_table.keys():
                frequency_table[str] += 1
            else:
                frequency_table[str] = 1

        global_max = -1
        print(frequency_table)

        for key in frequency_table.keys():
            if frequency_table[key] == 1:
                unique.append(key)

        def getLength(s):
            return len(s)

        unique.sort(key = getLength, reverse = True)

        print(unique)

        def isCommon(a, b):
            if len(a) > len(b):
                return False

            i = 0; j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            # i 如果等于a的长度，说明字符串b能够通过删减字符的方式得到a
            return i == len(a)

        for s in unique:
            isSubStr = False
            for str in strs:
                if s == str:
                    continue
                elif isCommon(s, str):
                    isSubStr = True
                    break

            if not isSubStr:
                global_max = len(s)
                break

        print(global_max)
        return global_max

if __name__ == '__main__':
    S = Solution()
    S.findLUSlength(["aaa","aaa","aa"])