# Last updated: 7/3/2025, 2:06:38 PM
class Solution(object):
    def checkRecord(self, s):
        a=0
        count=0
        for i in range(0,len(s)):
            if s[i] == "A":
                a+=1
        for j in range(0,len(s)-2):
            if s[j]==s[j+1]==s[j+2]=="L":
                count+=1
        if a>=2 or count>=1:
            return False
        else:
            return True

        