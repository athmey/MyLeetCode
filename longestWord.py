class Solution(object):
    # 长度小的在后面；长度相同的情况下，字典序大的在后面
    # 自定义的比较函数也很简单，只需要记住，根据需要条件，
    # 如果要把s1放到s2后面就return 1，如果要把s1放到s2前面就return -1，相同的话return 0
    def string_cmp(self, s1, s2):
        if len(s1) < len(s2):
            return 1

        elif len(s1) > len(s2):
            return -1

        else:
            if s1 > s2:
                return 1
            elif s1 < s2:
                return -1
            return 0

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(cmp=self.string_cmp)

        # words的第一个单词肯定是长度最长的单词
        for item in words:
            top = len(item)
            flag = True

            # 从最长的单词开始搜索，一步步递减
            while top > 0:
                if item[0:top] in words:
                    top -= 1
                    continue
                else:
                    flag = False
                    break

            if flag == True:
                return item
        return ''
