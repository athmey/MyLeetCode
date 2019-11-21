# 665. 非递减数列
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 题目的数组长度最多为10000
        '''
        我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
        '''
        if len(nums) <= 2:
            return True

        count = 0
        result = []

        for j in range(1, len(nums)):
            # 前一项比后一项大
            if nums[j] < nums[j - 1]:
                count += 1
                result.append(j)
        # 本身即为非递减数列
        if count == 0:
            return True

        elif count > 1:
            return False

        # count ==1
        else:
            i = result[0]

            # 在数组头尾都可以挽救
            if i == 1 or i == len(nums) - 1:
                return True

            elif nums[i + 1] >= nums[i - 1]:
                return True

            elif nums[i - 2] <= nums[i]:
                return True

            else:
                return False