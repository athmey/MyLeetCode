# 754. 到达终点数字

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0

        t = abs(target)
        k = 0
        s = 0
        while s < t:
            k += 1
            s += k
        dt = s - t
        if dt % 2 == 0:
            return k  # 1,2
        else:
            if k % 2 == 0:
                return k + 1  # 3,4
            else:
                return k + 2


