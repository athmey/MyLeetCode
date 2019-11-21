class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        roman_to_int_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                             'IV':4, 'IX':9, 'XL':40, 'XC':90,'CD':400, 'CM':900}

        result = 0

        index = 0

        # 从第一位遍历到字符串倒数第二位
        while index < len(s) - 1:
            # 如果当前位是I, X, C，判断其是否可能构成六大特殊情况
            if s[index] == 'I' or s[index] == 'X' or s[index] == 'C':
                temp = s[index] + s[index + 1]

                if temp in roman_to_int_dict.keys():
                    result += roman_to_int_dict[temp]

                    index += 2

                else:
                    result += roman_to_int_dict[s[index]]
                    index += 1

            else:
                result += roman_to_int_dict[s[index]]
                index += 1

        # 如果最后一位没有被处理
        if index == len(s) - 1:
            result += roman_to_int_dict[s[index]]
        return result

