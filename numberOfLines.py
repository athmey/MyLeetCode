class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        if widths is None or S is None or len(widths) is not 26 or len(S) is 0:
            return []

        current_line_length = 0
        total_row_num = 1

        for index in range(0, len(S)):
            width = widths[ord(S[index]) - ord('a')]

            if current_line_length + width <= 100:
                current_line_length += width

            else:
                total_row_num +=1
                current_line_length = 0
                current_line_length += width

        result = []
        result.append(total_row_num)
        result.append(current_line_length)

        return result