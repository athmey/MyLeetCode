class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) is 0:
            return 0

        if target > nums[-1]:
            return len(nums)

        if target < nums[0]:
            return 0

        # Use the binary search
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = ((start + end)//2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid -1

        return start
