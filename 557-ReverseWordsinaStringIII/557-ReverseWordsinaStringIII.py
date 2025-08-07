# Last updated: 8/7/2025, 2:47:22 AM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        b=""
        for i in range(0,len(a)):
            c=a[i][::-1]
            b+=c
            b+=" "
            d=b.rstrip()
        return d

        