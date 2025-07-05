# Last updated: 7/4/2025, 11:47:12 PM
class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        for i in range(32):
            if 2**i==n:
                return True
        return False