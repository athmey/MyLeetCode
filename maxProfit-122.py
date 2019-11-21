class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 122. 买卖股票的最佳时机 II

        # 这道题仍然是一道比较明显的动态规划算法

        if prices is None or len(prices) <= 1:
            return 0

        # 股票价格相比前一天每天都有上升或者下降，把握住所有上升机会即能获得最大收益
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                max_profit += prices[i] - prices[i-1]

        return max_profit
