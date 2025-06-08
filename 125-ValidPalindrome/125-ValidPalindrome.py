# Last updated: 6/7/2025, 7:12:24 PM
class Solution(object):
    def isPalindrome(self, s):
        b=""
        for i in s:
            if i.isalnum():
                b+=i.lower()
        c=b[::-1]
        if b==c:
            return True
        else:
            return False
            
        