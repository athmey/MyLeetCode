# 455. 分发饼干

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        biscuits = list(s)

        list.sort(g)
        list.sort(biscuits)

        for child in g:
            if not self.findBiscuit(child, biscuits):
                break

        # 发出去了多少块饼干，就是满足了多少个孩子
        return len(s) - len(biscuits)

    def findBiscuit(self, child, biscuits):
        if len(biscuits) == 0 or max(biscuits) < child:
            return False

        if min(biscuits) >= child:
            biscuits.pop(0)
            return True

        for biscuit in biscuits:
            if biscuit >= child:
                biscuits.remove(biscuit)
                return True

        return False
