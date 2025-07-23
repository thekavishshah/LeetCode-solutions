# Last updated: 7/23/2025, 3:02:53 PM
class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return False
        if num==0:
            return True
        for i in range(0,num):
            a=str(i)
            b=a[::-1]
            c=int(b)
            if i+c==num:
                return True
        return False
        