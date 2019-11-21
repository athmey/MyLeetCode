class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        horizontal = 0
        vertical = 0

        moves = moves.strip()

        if moves is None or moves is '' or len(moves) is 0:
            return True

        for c in moves:
            if c == 'L':
                horizontal += 1
            elif c == 'R':
                horizontal -= 1
            elif c == 'U':
                vertical += 1
            elif c == 'D':
                vertical -= 1

        return horizontal is 0 and vertical is 0