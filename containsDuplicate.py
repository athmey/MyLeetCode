class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if nums is None or len(nums) is 0 or len(nums) is 1:
            return False

        result = set(nums)

        if len(result) == len(nums):
            return False
        else:
            return True