# 744. 寻找比目标字母大的最小字母

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        distances = []

        for letter in letters:
            distance = ord(letter) - ord(target)

            if distance < 0:
                distance += 26

            if distance != 0:
                distances.append(distance)

        min_distance = min(distances)

        res_order = ord(target) + min_distance

        if res_order > ord('z'):
            res_order -= 26

        return chr(res_order)
