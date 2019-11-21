class Solution(object):
    '''
        思路：回文字符串，第一想到的就是使用两个指针，前后各一个，当遇到前后字符不一致的时候，有两种情况，删除前面字符或者删除后面字符。
             由于删除一个字符后剩下的仍旧是字符串，可以直接递归处理了。然后用一个flag，当达到2时，就可以递归结束了。
    '''

    def isPalindrome(self, s, left, right, flag):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if flag == 1:
                    return False
                flag = 1
                return (self.isPalindrome(s, left + 1, right, flag) or
                        self.isPalindrome(s, left, right - 1, flag))
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, 0, len(s) - 1, 0)