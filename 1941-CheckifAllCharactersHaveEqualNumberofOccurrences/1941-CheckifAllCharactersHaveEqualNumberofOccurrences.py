# Last updated: 8/1/2025, 1:34:48 AM
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={}
        for i in range(0,len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        values=list(d.values())
        for v in values:
            if v!=values[0]:
                return False
        return True

        