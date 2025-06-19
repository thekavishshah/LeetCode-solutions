# Last updated: 6/19/2025, 3:14:04 AM
class Solution(object):
    def isPowerOfThree(self, n):
        if n==0:
            return False
        while n%3==0:
            n=n/3
        return n==1