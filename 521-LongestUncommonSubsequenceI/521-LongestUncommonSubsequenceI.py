# Last updated: 7/9/2025, 10:15:42 PM
class Solution(object):
    def findLUSlength(self, a, b):
        if a==b:
            return -1
        else:
            return max(len(a), len(b))