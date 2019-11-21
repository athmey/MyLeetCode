# 1207. 独一无二的出现次数

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr is None or len(arr) <= 1:
            return True

        table = {}
        # 建立统计各个元素出现次数的字典
        for num in arr:
            if num in table.keys():
                table[num] += 1

            else:
                table[num] = 1

        vals = [val for val in table.values()]

        return len(vals) == len(list(set(vals)))
