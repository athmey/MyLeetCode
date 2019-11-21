class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if s == "":
            return res

        lp = len(p)
        ls = len(s)

        if lp > ls:
            return res

        pdict = {}
        sdict = {}

        # 统计两个字符串中在lp长度内各个字母出现的次数
        for i in range(lp):
            if not p[i] in pdict:
                pdict[p[i]] = 1
            else:
                pdict[p[i]] += 1

        for i in range(lp):
            if not s[i] in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1

        # 维护s字符串上lp长度的滑动窗的各个字符出现次数
        i = 0
        while i < (ls - lp):
            # 先进性比较
            if pdict == sdict:
                res.append(i)

            # 比较完成后滑动窗口往前移动一步
            sdict[s[i]] -= 1

            # 如果计数已经等于零，将这个字母对应的key删除
            if sdict[s[i]] == 0:
                del sdict[s[i]]

            # 将窗口新终点上的字符信息维护到字典sdict中
            if not s[i + lp] in sdict:
                sdict[s[i + lp]] = 1
            else:
                sdict[s[i + lp]] += 1

            i += 1

        if sdict == pdict:
            res.append(i)
        return res
