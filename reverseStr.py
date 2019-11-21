class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        res = ''

        index = 0

        while l >= 2 * k:
            tmp = s[index: index + 2 * k]
            print(tmp)

            cur_res = self.reverse(tmp)

            res += cur_res
            print(cur_res)

            index += 2 * k
            l -= 2 * k

        # 开始处理截取剩余的部分
        if l < k:
            if index - 1 < 0:
                res += s[len(s)-1:: -1]
            else:
                res += s[len(s) - 1:index - 1: -1]

        elif l >= k and l < 2 * k:
            if index == 0:
                res += s[index + k - 1:: -1]
            else:
                res += s[index + k -1:index-1: -1]
            res += s[index + k:]

        return res

    def reverse(self, s):
        res = ''
        length = len(s)

        res += s[length // 2 - 1::-1]

        res += s[length // 2:]

        return res