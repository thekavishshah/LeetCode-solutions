# Last updated: 7/21/2025, 4:36:21 PM
class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s[:2]
        for i in range(2,len(s)):
            if s[i]==a[-1] and s[i]==a[-2]:
                continue
            a+=s[i]
        return a
