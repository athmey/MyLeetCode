# 575. 分糖果
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # 统计糖果种类的数量
        # 如果糖果种类数小于总数的一半，则妹妹最多只能拿到所有种类的糖果；反之种类数目多于总数的一半，则只能拿到总数一半种类的糖果

        category_num = len(set(candies))

        return min(len(candies)//2, category_num)




