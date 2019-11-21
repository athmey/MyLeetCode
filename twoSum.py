class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if numbers is None and len(numbers) == 0:
            return -1

        list.sort(numbers)

        low = 0
        high = len(numbers) - 1

        while low < high:
            if numbers[low] + numbers[high] > target:
                high -= 1

            elif numbers[low] + numbers[high] < target:
                low += 1

            else:
                return [low + 1, high + 1]


