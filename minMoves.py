class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        '''
        思路：一开始是蒙蔽的，以为用贪心算法做，每一次都对除了一个最大元素之外的所有元素+1（或者加最大元素与次大元素的差值），
        结果发现运行时间过长，看了别人的思路，感觉跟脑筋急转弯一样：
        
        逆向思考，每次移动让剩余的n-1个数加1，相当于每次移动让选定的那个数减1， 所以最少移动次数其实就是所有元素减去最小元素的和
        '''
        return sum(nums) - min(nums) * len(nums)