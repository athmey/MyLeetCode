# 5067. 统计只含单一字母的子串
# 暴力解法超时
class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        if len(S) == 1:
            return 1

        cnt = 1
        s = 0

        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                cnt += 1  # 统计有几个字母相同

            else:
                s += cnt * (cnt + 1) / 2  # 等差公式求和
                cnt = 1

        return int(s + cnt * (cnt + 1) / 2)  # 最后一个并不会自动加上
