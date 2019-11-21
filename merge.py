class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # First Consider the corner cases
        if m is 0:
            counter = 0
            for element in nums2:
                nums1[counter] = element
                counter +=1
            return

        elif n is 0:
            pass

        else:
            nums1_index = 0
            nums2_index = 0
            # variable to record the shift time
            shift_counter = 0

            while nums2_index in range(n) and nums1_index in range(m+n):
                def allZeroBits(index):
                    for i in range(index, m+n):
                        if nums1[i] is not 0:
                            return  False
                    return True

                # Insert the elements to the end of nums1
                if allZeroBits(nums1_index):
                    while nums2_index < n:
                        nums1[nums1_index] = nums2[nums2_index]
                        nums1_index += 1
                        nums2_index += 1

                        print('!')

                    return

                elif nums2[nums2_index] >= nums1[nums1_index]:
                    nums1_index += 1

                else:
                    shift_counter += 1
                    for index in range(m - 1 + shift_counter, nums1_index, -1):
                        nums1[index] = nums1[index - 1]

                    nums1[nums1_index] = nums2[nums2_index]
                    nums2_index += 1

if __name__ == '__main__':
    solution = Solution()
    nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
    solution.merge(nums1, 1, nums2, 90)

    print(nums1)





