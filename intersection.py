class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = list()

        for element in nums1:
            if element in nums2:
                result.append(element)
        return list(set(result))