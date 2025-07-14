# Last updated: 7/13/2025, 6:13:47 PM
class Solution(object):
    def thirdMax(self, nums):
        a=set(nums)
        b=list(a)
        b.sort()
        if len(b)>=3:
            return b[-3]
        else:
            return b[-1]


