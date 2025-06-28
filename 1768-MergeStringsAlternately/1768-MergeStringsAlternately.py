# Last updated: 6/27/2025, 10:46:06 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        a=""
        for i in range(max(len(word1),len(word2))):
            if i<len(word1):
                a+=word1[i]
            if i<len(word2):
                a+=word2[i]
        return a