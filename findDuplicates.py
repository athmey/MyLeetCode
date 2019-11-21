class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) <= 1:
            return []

        result = []

        # 没有出现的和出现两次的元素对应位置上的内容都将是正数
        for num in nums:
            index = abs(num) - 1

            nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        # 再将没有出现的元素找出来并剔除
        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                pass

        for i in range(len(nums)):
            if nums[i] > 0:
                result.remove(i + 1)

        return result