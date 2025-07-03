# Last updated: 7/3/2025, 4:28:13 PM
class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            s=s[1:]+s[0]
            if s==goal:
                return True

        return False