# Last updated: 7/2/2025, 3:40:25 PM
class Solution(object):
    def isSubsequence(self, s, t):
        a = ""
        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                a += t[i]
                j += 1
        if a == s:
            return True
        else:
            return False
