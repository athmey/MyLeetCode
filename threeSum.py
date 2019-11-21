class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 15. 三数之和
        res = []

        if nums is None or len(nums) < 3:
            return res

        list.sort(nums)

        for i in range(len(nums)-2):
            if i >= 1:
                if nums[i] == nums[i-1]:
                    continue

            # 当nums[i]都已经大于0时，后面两个数至少大于等于nums[i]，三个数相加肯定大于0
            if nums[i] > 0:
                break

            current_target = nums[i] * -1

            start = i + 1
            end = len(nums) - 1

            # 建一个小缓存，去重当前的答案集合
            buff = []
            while start < end:
                if nums[start] + nums[end] > current_target:
                    end -= 1

                elif nums[start] + nums[end] < current_target:
                    start += 1

                elif nums[start] + nums[end] == current_target:
                    tmp = []
                    tmp.append(nums[i])
                    tmp.append(nums[start])
                    tmp.append(nums[end])

                    # 在这里加上去重语句
                    if tmp not in buff:
                        res.append(tmp)

                    buff.append(tmp)
                    start += 1

        return res