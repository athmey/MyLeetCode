class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = list()

        nums1.sort()
        nums2.sort()

        start1 = 0; end1 = 0
        start2 = 0; end2 = 0
        counter1 = 0
        counter2 = 0

        #1 2 2 1 -> 1 1 2 2
        #2 2

        while start1 < len(nums1):
            if nums1[start1] not in nums2:
                start1 +=1

            else:
                end1 = start1
                current_elem = nums1[start1]
                while end1 < len(nums1) and nums1[start1] == nums1[end1]:
                    end1 +=1
                    counter1 +=1

                start1 = end1

                start2 = nums2.index(current_elem)
                end2 = start2

                while end2 < len(nums2) and nums2[start2] == nums2[end2]:
                    end2 +=1
                    counter2 +=1

                for i in range(min(counter1,counter2)):
                    result.append(current_elem)

                counter1 = 0; counter2 = 0

        return result



