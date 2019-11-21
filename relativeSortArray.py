# 1122. 数组的相对排序

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if arr2 is None or len(arr2) == 0:
            return arr1

        def compare(num1, num2):
            index1 = arr2.index(num1)
            index2 = arr2.index(num2)

            if index1 > index2:
                return 1
            elif index1 < index2:
                return -1
            else:
                return 0

        sublist1 = []
        sublist2 = []

        for num in arr1:
            if num in arr2:
                sublist1.append(num)
            else:
                sublist2.append(num)

        sublist1.sort(cmp = compare)
        sublist2.sort()
        sublist1.extend(sublist2)
        return sublist1
