'''
开辟一个栈，栈里存放的是数组元素的下标

然后线性扫描整个数组，如果栈是空的，或者栈顶元素对应的数组元素比当前元素大，那么就把当前元素的下标压入栈，

否则，就说明栈顶元素对应的数组元素的下一个更大元素就是当前元素，然后pop栈顶元素，重复这个过程直到栈顶元素对应的数组元素》=当前元素或者栈为空为止。

一趟线性扫描结束之后，如果栈不为空，就说明还要扫一次找到需要循环查找的结果，

就从头再扫一次，思路跟上面一样。
'''

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums

        #整个数组的最大元素
        max_element = max(nums)

        stack = list()
        res = [-1 for i in range(len(nums))]

        for i, x in enumerate(nums):

            if not stack or nums[stack[-1]] >= x:
                stack.append(i)
            else:
                # print stack, res
                while (stack and nums[stack[-1]] < x):
                    res[stack[-1]] = x
                    stack.pop()
                if x != max_element:  # 最大的不用放进栈，直接默认-1就好
                    stack.append(i)

        # print stack, res
        if stack:  # 还有需要循环搜索的元素
            for i, x in enumerate(nums):
                if not stack:
                    break
                while stack and x > nums[stack[-1]]:
                    res[stack[-1]] = x
                    stack.pop()

        return res
