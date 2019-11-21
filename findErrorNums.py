class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list.sort(nums)
        res = []

        total_sum = 0
        for i in range(1, len(nums)+1):
            total_sum += i

        diff = total_sum - sum(nums)

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                res.append(nums[i]+diff)
                return res

