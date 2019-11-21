class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        max_perimeter = 0

        # sort the input list
        A.sort()

        for index in range(len(A) - 3, -1, -1):
            if self.is_triangle(A[index], A[index+1], A[index+2]):
                return A[index] + A[index+1] + A[index+2]

        return 0


    def is_triangle(self, a,b,c):

        if a + b > c:
            return True
        else:
            return False