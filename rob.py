class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 0:
            return 0

        if len(nums) is 1:
            return nums[0]

        if len(nums) is 2:
            return max(nums[0], nums[1])

        else:
            maxVal_two_digits_ahead = nums[0] # the max value before this digit that can get
            max_exclude_current = nums[1] # the max value I can get except this digit
            max_include_current = 0
            current_max = 0

            for elem in nums[2:]:
                max_include_current = elem + maxVal_two_digits_ahead

                if max_include_current < max_exclude_current:
                    current_max = max_exclude_current

                else:
                    current_max = max_include_current

                # update the corresponding values
                maxVal_two_digits_ahead = max(maxVal_two_digits_ahead, max_exclude_current)
                max_exclude_current = max(max_include_current, max_exclude_current)

        return current_max

