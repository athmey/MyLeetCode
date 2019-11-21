class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return False

        if len(word) == 1:
            return True

        '''
        我们定义，在以下情况时，单词的大写用法是正确的：

            全部字母都是大写，比如"USA"。
            单词中所有字母都不是大写，比如"leetcode"。
            如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
        否则，我们定义这个单词没有正确使用大写字母。
        '''
        is_all_upper_case = True
        is_all_lower_case = True

        first_char_is_upper = word[0].isupper()


        for index in range(1,len(word)):
            # 第一个字母是大写
            if first_char_is_upper:
                is_all_lower_case = False

                if word[index].isupper() != word[1].isupper():
                    return False

            # 第一个字母是小写
            else:
                is_all_upper_case = False

                if word[index].isupper():
                    return False

        return is_all_upper_case or is_all_lower_case

