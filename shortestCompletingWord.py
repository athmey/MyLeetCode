# 748. 最短完整词
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # 先记录licensePlate中存在的字母
        alphabet_table = []
        for c in licensePlate:
            if c.isalpha():
                alphabet_table.append(c.lower())

        self.buffer = []

        def match(word, table):
            # 获取当前单词的小写字母列表
            word_list = [c.lower() for c in word]

            if len(word_list) < len(table):
                return False

            else:
                table_copy = list(table)

                for i in range(len(table_copy)):
                    if table_copy[i] in word_list:
                        word_list.remove(table_copy[i])

                    else:
                        return False

                return True

        for word in words:
            if match(word, alphabet_table):
                self.buffer.append(word)

        # buffer中按先后顺序存储了所有符合条件的单词
        def getLength(s):
            return len(s)

        list.sort(self.buffer, key=getLength)

        index = len(words)-1
        for i in range(len(self.buffer)):
            if len(self.buffer[i]) == len(self.buffer[0]):
                if words.index(self.buffer[i]) < index:
                    index = words.index(self.buffer[i])

        return words[index]




