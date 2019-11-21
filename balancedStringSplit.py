# 1221. 分割平衡字符串

'''
    该题借鉴了大佬的思路，可以用数模拟栈的实现

    遍历该字符串，当出现R时，stack就++；当出现L时，stack--

    这样，当stack==0的时候，就说明该子串是平衡的。故可以用变量n记录平衡子串的个数； n++
'''
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) <= 1:
            return 1

        balance_stack = 0
        result = 0

        for c in s:
            if c == 'L':
                balance_stack += 1

            else:
                balance_stack -= 1

            if balance_stack == 0:
                result += 1

        return result








