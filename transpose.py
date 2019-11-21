class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None:
            return None

        if len(A) is 0:
            return list()

        input_rows = len(A)
        input_cols = len(A[0])

        output_rows = input_cols
        output_cols = input_rows

        output = [[0 for col in range(output_cols)]for row in range(output_rows)]

        for i in range(input_rows):
            for j in range(input_cols):
                output[j][i] = A[i][j]

        return output