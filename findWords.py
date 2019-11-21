class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []

        if words is None or len(words) == 0:
            return result

        row1 = ['Q','W','E','R','T','Y','U','I','O','P']
        row2 = ['A','S','D','F','G','H','J','K','L']
        row3 = ['Z','X','C','V','B','N','M']

        keyboard = []
        keyboard.append(row1)
        keyboard.append(row2)
        keyboard.append(row3)

        for word in words:
            flag = True
            rownum = -1

            for index in range(len(keyboard)):
                if word[0].upper() in keyboard[index]:
                    rownum = index
                    print('Num: ', rownum)

            for i in range(1, len(word)):
                if word[i].upper() not in keyboard[rownum]:
                    flag = False
                    break

            if flag == True:
                result.append(word)

        return result
