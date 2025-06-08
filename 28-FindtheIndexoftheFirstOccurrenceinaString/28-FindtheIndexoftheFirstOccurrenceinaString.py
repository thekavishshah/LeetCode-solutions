# Last updated: 6/7/2025, 10:34:00 PM
class Solution(object):
    def strStr(self, a, b):
        if b in a:
            return(a.index(b))
        else:
            return(-1)
        