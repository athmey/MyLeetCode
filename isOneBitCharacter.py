class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # 遇1进二直接跳到下一个数，判断最后是否指向最后一个元素
        i = 0
        while i < len(bits):
            if i == len(bits)-1:
                return True
            elif bits[i] == 1:
                i += 2
            else:
                i += 1
        return False