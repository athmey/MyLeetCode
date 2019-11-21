class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        if queries is None or len(queries) is 0:
            return A

        if A is None or len(A) is 0:
            return A

        result = list()
        sum = 0

        for num in A:
            if num % 2 is 0:
                sum += num

        for count in range(len(queries)):
            val = queries[count][0]
            index = queries[count][1]

            updated_val = A[index] + val

            if A[index] % 2 is 0:
                sum -= A[index]

            # update the A[index]
            A[index] = updated_val

            if updated_val%2 is 0:
                sum += updated_val

            else:
                pass

            result.append(sum)

        return result