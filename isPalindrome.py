class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False

        s = s.strip()

        if len(s) is 0 or len(s) is 1:
            return True

        # extract the valid char from input
        pure_s = [char.lower() for char in s if char.isalnum()]

        return pure_s == pure_s[::-1]


