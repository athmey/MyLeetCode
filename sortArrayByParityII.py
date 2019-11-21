class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A is None or len(A) == 0:
            return A

        even_nums = []
        odd_nums = []

        for num in A:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)

        res = []

        counter = 0
        index_even = 0
        index_odd = 0

        while index_even < len(even_nums) or index_odd < len(odd_nums):
            if counter % 2 == 0:
                res.append(even_nums[index_even])
                index_even += 1
            else:
                res.append(odd_nums[index_odd])
                index_odd += 1
            counter += 1

        return res