class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 746. 使用最小花费爬楼梯

        # 这道题应该是一个很明显的使用动态规划的题目

        # min_cost中存储爬到当前第i层楼梯所需要的最小的体力值
        min_cost = [0 for i in range(len(cost))]
        min_cost[0] = cost[0]
        min_cost[1] = min(cost[1], min_cost[0] + cost[1])

        for i in range(2, len(cost)):
            min_cost[i] = min(min_cost[i-1] + cost[i], min_cost[i-2] + cost[i])

        return min(min_cost[-2], min_cost[-1])

