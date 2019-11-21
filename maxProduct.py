class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        global_max = nums[0]
        local_max = nums[0]
        local_min = nums[0]

        for i in range(1, len(nums)):
            max_copy = local_max

            local_max = max(local_min * nums[i], local_max * nums[i], nums[i])
            local_min = min(local_min * nums[i], max_copy * nums[i], nums[i])

            global_max = max(global_max, local_max)

        return global_max






