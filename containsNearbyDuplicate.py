class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = set()
        for index, num in enumerate(nums):
            if num in record:
                return True

            record.add(num)

            if len(record) == k + 1:
                record.remove(nums[index - k])

        return False
