# Last updated: 7/16/2025, 4:48:50 PM
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in range(0,len(s)):
            if d[s[i]]==1:
                return i
        return -1

        