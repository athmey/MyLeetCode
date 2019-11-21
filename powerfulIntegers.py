class Solution:
    def powerfulIntegers(self, x, y, bound):
        res_set = set()

        for i in range(bound):
            tmp1 = x ** i
            if tmp1 > bound:
                break
            for j in range(bound):
                tmp2 = y ** j
                tmp = tmp1 + tmp2
                if tmp > bound:
                    break
                res_set.add(tmp)

        return list(res_set)