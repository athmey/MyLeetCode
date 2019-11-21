class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 先对列表进行排序，防止得到不是最小的移动步数，
        # 然后根据列表长度分奇偶得到对应中位数，求得列表元素与中位数相减取绝对值求和则为最小移动步数。

        nums.sort()

        index = len(nums) // 2
        ans = 0

        for i in nums:
            ans += abs(i - nums[index])
        return ans
