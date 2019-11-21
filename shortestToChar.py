class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        if S is None or len(S) is 0 or C is None or C is '' or C not in S:
            return []

        S = S.strip()
        C = C.strip()

        target_positions = []

        for index in range(len(S)):
            if S[index] == C:
                target_positions.append(index)

        result = []
        list.sort(target_positions)

        for index in range(len(S)):
            if index <= target_positions[0]:
                result.append(abs(index - target_positions[0]))
            elif index >= target_positions[-1]:
                result.append(abs(index - target_positions[-1]))
            else:
                global_min = len(S)

                for elem in target_positions:
                    global_min = min(abs(index - elem), global_min)

                result.append(global_min)

        return result
