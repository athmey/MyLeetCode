class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) < k:
            return

        temp = nums[0:k]
        list.sort(temp)

        for elem in nums[k:]:
            if elem > temp[-1]:
                temp.append(elem)
                temp.pop(0)

            elif elem < temp[0]:
                continue

            else:
                for index in range(len(temp)-1):
                    if elem > temp[index] and elem <= temp[index + 1]:
                        temp.insert(index+1, elem)
                        temp.pop(0)

        return temp[0]

