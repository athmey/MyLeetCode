class Solution(object):
    def sortArrayByParity(self, A):
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

        even_nums.extend(odd_nums)
        return even_nums