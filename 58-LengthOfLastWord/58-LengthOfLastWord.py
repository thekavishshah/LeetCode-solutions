# Last updated: 6/7/2025, 7:02:42 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.split()
        b=a[-1]
        c=len(b)
        return c