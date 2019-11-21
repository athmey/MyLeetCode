class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if K > len(points) or K is 0 or points is None:
            return list()


        points.sort(key = lambda pair: pair[0]**2 + pair[1]**2)
        return points[0:K]
