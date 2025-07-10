# Last updated: 7/9/2025, 10:11:48 PM
class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper()==True or word.islower()==True or word.istitle()==True:
            return True
        else:
            return False