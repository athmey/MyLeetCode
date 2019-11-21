class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return s

        Vowels = ['a','e','i','o','u']
        Vowels = set(Vowels)

        Vowels_position = []

        for index in range(len(s)):
            if s[index].lower() in Vowels:
                Vowels_position.append(index)

        copy = list(s)
        for i in range(len(Vowels_position)//2):
            temp = copy[Vowels_position[i]]
            copy[Vowels_position[i]] = copy[Vowels_position[len(Vowels_position) - 1 - i]]
            copy[Vowels_position[len(Vowels_position) - 1 - i]] = temp

        result = ''
        for c in copy:
            result = result + str(c)

        return result