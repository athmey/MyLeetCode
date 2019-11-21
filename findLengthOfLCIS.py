# 674. 最长连续递增序列
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        global_max = 1

        start = 0
        end = 1

        while end < len(nums):
            # 后一项比前一项大
            if nums[end] > nums[end-1]:
                end += 1

            # 后一项不比前一项大
            else:
                current_length = ((end-1) - start) + 1

                if current_length > global_max:
                    global_max = current_length

                start = end
                end += 1

        return max(global_max, ((end-1) - start) + 1)

