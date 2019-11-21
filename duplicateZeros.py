# 1089. 复写零

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        positions = []
        for i in range(len(arr)):
            if arr[i] == 0:
