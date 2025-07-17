# Last updated: 7/16/2025, 10:00:30 PM
class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero=0
        one=0
        for i in range(0,len(s)):
            if s[i]=="1":
                one+=1
            else:
                zero+=one
        return zero
        