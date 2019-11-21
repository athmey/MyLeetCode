class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False

        s = s.strip()

        if len(s) % 2 is not 0:
            return False

        leftparenthesis = ['(', '[', '{']
        charQueue = list()

        for c in s:
            if c in leftparenthesis:
                charQueue.append(c)
            # if current char is right parenthesis
            else:
                if len(charQueue) is 0:
                    return False
                elif c is ')' and charQueue[-1] is '(':
                    charQueue.pop()
                elif c is ']' and charQueue[-1] is '[':
                    charQueue.pop()
                elif c is '}' and charQueue[-1] is '{':
                    charQueue.pop()
                else:
                    return False

        if len(charQueue) is 0:
            return True
        else:
            return False


