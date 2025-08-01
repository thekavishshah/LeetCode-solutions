# Last updated: 8/1/2025, 1:10:18 AM
class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:

            product=1
            temp=n
            while temp:
                a=temp%10
                product*=a
                temp=temp//10
            if product%t==0:
                return n
            n+=1

        
        
        