class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        set_ransomNote = set(ransomNote)
        set_magazine = set(magazine)

        for c in set_ransomNote:
            if c not in set_magazine:
                return False

        dict_ransomNote = {}
        dict_magazine = {}

        for c in ransomNote:
            if c in dict_ransomNote.keys():
                dict_ransomNote[c] += 1
            else:
                dict_ransomNote[c] = 1

        for c in magazine:
            if c in dict_magazine.keys():
                dict_magazine[c] += 1
            else:
                dict_magazine[c] = 1

        for key in dict_ransomNote.keys():
            if dict_ransomNote[key] > dict_magazine[key]:
                return False

        return True



