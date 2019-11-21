class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
            return result

        for num in nums1:
            index = nums2.index(num)

            result.append(self.lauchIndex(nums2[index + 1:], num))

        return result


    def lauchIndex(self, input, val):
        for elem in input:
            if elem > val:
                return elem

        return -1