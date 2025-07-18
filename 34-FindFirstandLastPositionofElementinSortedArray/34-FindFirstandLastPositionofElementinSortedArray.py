# Last updated: 7/17/2025, 11:06:34 PM
class Solution(object):
    def searchRange(self, nums, target):
        start=-1
        end=-1
        for i in range(0,len(nums)):
            if nums[i]==target:
                if start==-1:
                    start=i
                end=i
        return [start,end]