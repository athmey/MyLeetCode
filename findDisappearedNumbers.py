class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 思路：标记法，由于所有元素当范围在[1,n]之间，所以考虑标记出现过的元素，最后没有出现过当元素即为所求
        if nums is None or len(nums) is 0:
            return []

        result = []

        for i in range(len(nums)):
            # 获取当前元素应该对应的索引值
            index = abs(nums[i]) - 1

            # 将出现过的元素取相反数
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                pass

        for index in range(len(nums)):
            if nums[index] > 0:
                result.append(index + 1)

        return result