class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) is 0:
            return

        if len(nums) is 1:
            return nums[0]

        if len(nums) is 2:
            return max(nums[0], nums[1])

        # res 数组是降序的， 大->小
        res = [float("-inf")] * 3

        for i in nums:
            if i in res:
                continue
            if i > res[0]:
                res = [i, res[0], res[1]]
            elif i > res[1]:
                res = [res[0], i, res[1]]
            elif i > res[2]:
                res = [res[0], res[1], i]
            print(res)

        return res[-1] if res[2] != float("-inf") else res[0]

