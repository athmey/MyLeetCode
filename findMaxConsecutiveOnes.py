class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        if nums is None or len(nums) == 0:
            return  result

        start = 0
        end = 0

        while end < len(nums):
            #print("end: %d; start: %d"%(end,start))
            if nums[end] == 1:
                while end < len(nums) and nums[end] == 1:
                    end += 1

                result = max(result, end - start)

            else:
                end += 1
                start = end

        return result