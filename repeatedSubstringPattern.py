class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True

        # Range: 1-len(s)//2
        for length in range(1, (len(s) // 2) + 1):
            copy = str(s)
            current_sub_str = copy[:length]

            while True:
                if copy[:length] == current_sub_str:
                    copy = copy[length:]
                else:
                    break

            if len(copy) == 0:
                return True

        return False