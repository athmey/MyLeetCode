# 724. 寻找数组的中心索引
# 动态规划
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        sum_left = 0
        sum_right = 0

        for i in range(1, len(nums)):
            sum_right += nums[i]

        for i in range(0, len(nums)-1):
            if sum_left == sum_right:
                return i

            else:
                sum_left += nums[i]
                sum_right -= nums[i+1]

        if sum_left == 0:
            return len(nums)-1

        return -1