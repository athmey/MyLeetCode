class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 记录有多少个0即可

        zero_num = 0
        for num in nums:
            if num == 0:
                zero_num += 1

        index = 0

        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        for index in range(len(nums) - zero_num, len(nums)):
            nums[index] = 0