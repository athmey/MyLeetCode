# 1013. 将数组分成和相等的三个部分

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total_sum = sum(A)

        if total_sum % 3 != 0:
            return False

        target = total_sum // 3

        break_point1 = 0
        break_point2 = 0

        temp = 0

        has_valid_break_point1 = False
        for i in range(len(A)-2):
            temp += A[i]

            if temp == target:
                break_point1 = i+1
                has_valid_break_point1 = True
                break

        if not has_valid_break_point1:
            return False

        has_valid_break_point2 = False
        temp = 0
        for i in range(break_point1,len(A)-1):
            temp += A[i]

            if temp == target:
                break_point2 = i+1
                has_valid_break_point2 = True
                break

        if not has_valid_break_point2:
            return False

        print(break_point1, break_point2)

        # 处理最后剩下的这段数组
        if sum(A[break_point2:]) == target:
            return True
        else:
            return False


