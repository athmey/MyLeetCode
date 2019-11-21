# 819. 最常见的单词

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.split()

        table = {}

        for word in words:
            # 去掉词尾的标点
            if not word[-1].isalpha():
                word = word[:-1]
            # 将词转化为小写
            word = word.lower()

            chars = word.split(',')
            if len(chars) > 1:
                for char in chars:
                    if char in table.keys():
                        table[char] += 1
                    else:
                        table[char] = 1
            else:
                if word in table.keys():
                    table[word] += 1
                else:
                    table[word] = 1

        # 对table内的词按出现次数降序排序
        sorted_pairs = sorted(table.items(), key=lambda x:x[1],reverse=True)

        print(sorted_pairs)

        for pair in sorted_pairs:
            if pair[0] not in banned:
                return pair[0]

if __name__ == '__main__':
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]

    solution = Solution()
    solution.mostCommonWord(paragraph, banned)
