# Last updated: 5/2/2025, 1:17:37 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed =0
        original =x
        while x>0:
            last_digit = x%10
            reversed = reversed*10 + last_digit
            x = x//10
        return reversed==original

    
        