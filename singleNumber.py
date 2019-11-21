class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 1:
            return nums[0]

        else:
            temp = nums[0]
            for num in nums[1:]:
                temp = temp ^ num

            return temp
