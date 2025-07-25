# Last updated: 7/24/2025, 11:40:56 PM
class Solution(object):
    def reverseWords(self, s):
        s=s.lstrip()
        s=s.rstrip()
        s=s.split()
        a=""
        for i in range(len(s)-1,-1,-1):
            a=a+s[i]+" "
        return a.rstrip()

