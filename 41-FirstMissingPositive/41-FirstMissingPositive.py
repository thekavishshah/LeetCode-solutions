# Last updated: 7/8/2025, 11:34:14 PM
class Solution(object):
    def firstMissingPositive(self, nums):
        a=set(nums)
        i=1
        while True:
            if i not in a:
                return i
            i+=1
