class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if A is None or len(A) == 0 or K == 0:
            return A

        result = []

        k = str(K)

        counter = 1
        carry = 0

        while counter <= min(len(A), len(k)):
            sum = A[len(A) - counter] + int(k[len(k) - counter]) + carry

            carry = sum // 10
            sum = sum % 10

            result.append(sum)
            counter += 1

        if len(A) > len(k):
            while counter <= len(A):
                sum = A[len(A) - counter] + carry

                carry = sum // 10
                sum = sum % 10

                result.append(sum)
                counter += 1
        else:
            while counter <= len(k):
                sum = int(k[len(k) - counter]) + carry

                carry = sum // 10
                sum = sum % 10

                result.append(sum)
                counter += 1

        if carry != 0:
            result.append(carry)

        return result[::-1]