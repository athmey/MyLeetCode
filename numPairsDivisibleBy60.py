class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        ret = {}
        result = 0
        for i in range(len(time)):
            # 判断当前歌曲长度能否被60整除
            mod = time[i] % 60

            # 如果不能整除
            if mod != 0:
                need_number = 60 - mod
            # 如果可以整除
            else:
                need_number = 0

            if mod in ret:
                result += ret[mod]

            # 当前数字能和need_number凑成一组，记录一下有多少数字能和need_number凑成满足题意的数字对
            if need_number in ret:
                ret[need_number] += 1
            else:
                ret[need_number] = 1

        return result
