class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) is 0 or len(nums) is 1:
            return len(nums)


        current_index = 0
        next_index = 1 + current_index
        new_length = len(nums)

        while next_index < len(nums):

            if nums[next_index] == nums[current_index]:
                next_index += 1
                new_length -= 1
            else:
                current_index += 1
                nums[current_index] = nums[next_index]
                next_index += 1
        print('New Length: ', new_length)
        return new_length
