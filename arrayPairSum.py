class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 升序排序后两两配对，每一对最小值组成的和能够满足题意
        list.sort(nums)

        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]

        return res
