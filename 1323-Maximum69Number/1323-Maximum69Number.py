# Last updated: 8/2/2025, 1:06:53 AM
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        a=str(num)
        b=a.replace("6","9",1)
        return int(b)
        