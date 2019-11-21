class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__mylist = list(nums)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        result = 0
        for index in range(i,j+1):
            result += self.__mylist[index]
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)