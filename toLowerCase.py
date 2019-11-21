class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        if str is None:
            return str

        str = str.strip()

        if len(str) == 0:
            return str

        diff = ord('a') - ord('A')

        res = ''

        for c in str:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                res += chr(ord(c) + diff)

            else:
                res += c

        return res