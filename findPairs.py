class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or k < 0:
            return 0

        candidate = list(set(nums))
        list.sort(candidate)

        res = 0

        for num in candidate:
            if k == 0:
                if nums.count(num) >= 2:
                    res += 1

            else:
                if num + k in candidate:
                    res += 1

                if num + k > candidate[-1]:
                    break

        return res