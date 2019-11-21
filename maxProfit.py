class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) <= 1:
            return 0

        min = prices[0]
        max_profit = 0

        for elem in prices:
            # 更新股票最低价
            if elem < min:
                min = elem
            # 当前股价比最低价高的话，就计算收益
            else:
                if elem - min > max_profit:
                    max_profit = elem - min

        return max_profit