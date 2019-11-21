class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        chart = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res = []

        for word in words:
            tmp = ''
            for c in word:
                c = c.lower()

                tmp += chart[ord(c) - ord('a')]

            res.append(tmp)

        return len(set(res))