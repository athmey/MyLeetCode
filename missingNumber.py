class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_in_list = 0

        for elem in nums:
            sum_in_list += elem

        correct_sum = 0
        for i in range(len(nums) + 1):
            correct_sum += i

        return correct_sum - sum_in_list