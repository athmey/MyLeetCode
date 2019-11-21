class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []

        for i in range(left, right+1):
            val = i
            flag = 1

            while i != 0:
                # 先求余数
                remain = i % 10

                # 当前位为0 或者 当前位被原数除余数不为0， 都算作不符合条件
                if not remain or val % remain != 0:
                    flag = 0
                    break

                i /= 10

            if flag:
                ret.append(val)

        return ret