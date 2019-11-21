class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if str is None or pattern is None:
            return True

        str = str.strip()
        pattern = pattern.strip()

        words = str.split()
        str_length = len(words)
        pattern_length = len(pattern)

        if pattern_length != str_length:
            return False

        pattern_records = dict()

        # 根据pattern建立一张字符与对应位置的映射表
        for index, val in enumerate(pattern):
            if pattern.count(val) != words.count(words[index]):
                return False

            if val not in pattern_records.keys():
                pattern_records[val] = [index]
            else:
                pattern_records[val].append(index)


        for char in pattern_records.keys():
            # 取出当前pattern中字符，并查询其在str中的映射
            corresponding_word_in_str = words[pattern_records[char][0]]

            for i in range(1, len(pattern_records[char])):
                if words[pattern_records[char][i]] != corresponding_word_in_str:
                    return False

        return True

