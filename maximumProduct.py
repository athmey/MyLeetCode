class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list.sort(nums)

        if nums[-1] >= 0:
            if nums[0] < 0 and nums[1] < 0:
                return max(nums[-1]*nums[0]*nums[1], nums[-1]*nums[-2]*nums[-3])

            else:
                return nums[-1]*nums[-2]*nums[-3]

        else:
            return nums[-1]*nums[-2]*nums[-3]