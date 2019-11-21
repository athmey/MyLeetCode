'''
997. 找到小镇的法官

在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

1. 小镇的法官不相信任何人。
2. 每个人（除了小镇法官外）都信任小镇的法官。
3. 只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-town-judge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
    # 先找出符合条件1的人
        buffer1 = []
        buffer2 = []
        for pair in trust:
            buffer1.append(pair[0])
            buffer2.append(pair[1])

        buffer1 = list(set(buffer1))
        temp = [i for i in range(1, N+1)]

        cond1_buffer = set(temp) - set(buffer1)

        if len(cond1_buffer) < 1:
            return -1

    # 从符合条件1的人中，再找出符合条件2的人,这个人的序号需要出现N-1次
        for p in list(cond1_buffer):
            if buffer2.count(p) == N - 1:
                return p
        return -1

if __name__ == '__main__':
    N = 1
    trust = []

    solution = Solution()
    solution.findJudge(N, trust)
