'''
思路：根据字符串s构建一个字典，字典中的键为s中的字符，值为该字符在字典中出现的位置，
然后用这个字典去检验t，看是否一个键所对应的所有位置均相同。

思路：根据字符串s构建一个字典，字典中的键为s中的字符，值为该字符在字典中出现的位置，
然后用这个字典去检验t，看是否一个键所对应的所有位置均相同。
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False

        if len(s) is 0 or len(s) is 1:
            return True

        if len(s) != len(t):
            return False

        count_dic = {}
        for index, item in enumerate(s):
            # 相同位置的字符在整个字符串中出现的次数不一样多
            if not s.count(item) == t.count(t[index]):
                return False

            if not item in count_dic.keys():
                count_dic[item] = [index]
            else:
                count_dic[item].append(index)

        # 根据字典的key遍历字典
        for item in count_dic:
            # 找到s字符内当前字符t字符中同位置的映射，如果不匹配则返回False
            tmp = t[count_dic[item][0]]
            for i in range(1, len(count_dic[item])):
                if not t[count_dic[item][i]] == tmp:
                    return False
        return True

