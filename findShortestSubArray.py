# 697. 数组的度
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        # 建表查找出现次数最多的元素 key:元素 value：该元素出现的所有位置构成的列表
        table = {}

        for i, v in enumerate(nums):
            if v in table.keys():
                table[v].append(i)
            else:
                table[v] = [i]

        max_length = 0
        buffer = []
        for l in table.values():
            if len(l) > max_length:
                max_length = len(l)

        for key in table.keys():
            if len(table[key]) == max_length:
                buffer.append(table[key])

        min = 50000
        for l in buffer:
            if l[-1] - l[0] + 1 < min:
                min = l[-1] - l[0] + 1

        return min





