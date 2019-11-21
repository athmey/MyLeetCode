# 1071. 字符串的最大公因子
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        a = str1 if len(str1) >= len(str2) else str2
        b = str2 if len(str2) <= len(str1) else str1  # a是长串, b是短串


        x = ''
        res = ''

        for i in range(len(b)):
            if b[i] == a[i]:  # 按位比较是否相同
                x += b[i]

                # 不停的更新res
                if ''.join(a.split(x)) == '' and ''.join(b.split(x)) == '':  # 判断为共有子串,并记录
                    res = x

            # 两个字符串第一个字母都不一样的话只能判断最大公因子为空串
            else:
                return ''

        return res
