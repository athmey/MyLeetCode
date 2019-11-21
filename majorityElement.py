class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 0 or nums is None:
            return 0

        if len(nums) is 1:
            return nums[0]

        nums.sort()

        threshold = len(nums)//2 + 1
        counter = 1

        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                counter += 1

                if counter == threshold:
                    return nums[index]

            else:
                counter = 1

