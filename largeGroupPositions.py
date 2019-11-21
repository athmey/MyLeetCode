# 830. 较大分组的位置

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []

        if len(S) <= 2:
            return res

        start = 0
        end = 0

        while end < len(S):
            # 如果碰到的是相同字母:
            if S[end] == S[start]:
                end += 1

            # 如果碰到了不相同的字母:
            else:
                if (end-1)-start+1 >= 3:
                    buffer = []
                    buffer.append(start)
                    buffer.append(end - 1)

                    res.append(buffer)

                start = end
        if (end - 1) - start + 1 >= 3:
            res.append([start, end-1])
        return res

