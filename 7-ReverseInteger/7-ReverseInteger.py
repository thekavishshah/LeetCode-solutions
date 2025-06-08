# Last updated: 6/8/2025, 12:09:17 AM
class Solution(object):
    def reverse(self, x):
        

        if x>0:

            a=str(x)
            b=a[::-1]
            c=int(b)
        else:
            a=str(-x)
            b=a[::-1]
            c=-int(b)

        if c<(-2**31) or c>(2**31 -1):
            return 0
        return c
        
        
        
        