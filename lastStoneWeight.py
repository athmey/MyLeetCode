class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 先试试暴力解法
        if len(stones) == 1:
            return stones[0]

        while True:
            if len(stones) == 0:
                return 0

            elif len(stones) == 1:
                return stones[0]

            else:
                stone1 = max(stones)
                stones.remove(stone1)

                stone2 = max(stones)
                stones.remove(stone2)

                # 两者质量相等，两块石头同时消失
                if stone2 == stone1:
                    pass
                else:
                    stones.append(stone1 - stone2)