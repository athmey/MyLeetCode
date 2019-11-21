class Solution:

    '''
        ord():字符到整数
        chr():整数到字符
    '''
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int

        """
        if s.strip() == '' or len(s.strip()) == 0:
            return 0

        start_num = ord('A') - 1

        power = len(s.strip()) - 1
        sum = 0
        for char in s:
            sum += (ord(char) - start_num) * pow(26, power)
            power -= 1

        return sum



