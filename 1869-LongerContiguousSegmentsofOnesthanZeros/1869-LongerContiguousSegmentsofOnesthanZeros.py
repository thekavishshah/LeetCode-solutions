# Last updated: 8/2/2025, 1:18:25 AM
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        current_length1=0
        max_length1=0
        current_length0=0
        max_length0=0

        for i in range(0,len(s)):
            if s[i]=="1":
                current_length1+=1
                current_length0=0
                if current_length1>max_length1:
                    max_length1=current_length1
            if s[i]=="0":
                current_length0+=1
                current_length1=0
                if current_length0>max_length0:
                    max_length0=current_length0
        return max_length1>max_length0
