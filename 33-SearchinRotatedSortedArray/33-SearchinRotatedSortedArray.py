# Last updated: 6/8/2025, 12:43:49 AM
class Solution(object):
    def search(self, nums, target):
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
        return -1
        