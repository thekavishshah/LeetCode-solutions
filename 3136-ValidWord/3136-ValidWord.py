# Last updated: 7/22/2025, 12:08:13 AM
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        if word.isalnum()==False:
            return False
        vowels=False
        consonants=False
        for i in word:

            a="aeiouAEIOU"
            if i.isalpha():
                if i in a:
                    vowels=True
                else:
                    consonants=True
        if vowels and consonants:
            return True
        else:
            return False
