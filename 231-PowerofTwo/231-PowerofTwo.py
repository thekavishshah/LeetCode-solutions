# Last updated: 8/8/2025, 5:17:47 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        for i in range(32):
            if 2**i==n:
                return True
        return False
        