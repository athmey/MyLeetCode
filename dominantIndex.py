class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 747. 至少是其他数字两倍的最大数
        if len(nums) == 1:
            return 0

        copy = list(nums)
        list.sort(copy)

        if copy[-1] >= 2 * copy[-2]:
            return nums.index(copy[-1])
        else:
            return -1
