# Last updated: 6/12/2025, 3:08:39 PM
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)