# 581. 最短无序连续子数组

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        copy = list(nums)
        list.sort(nums)

        buffer = []

        for i in range(len(nums)):
            if nums[i] != copy[i]:
                buffer.append(i)

        if len(buffer) == 0:
            return 0
        else:
            return (buffer[-1]-buffer[0])+1
