# Last updated: 6/9/2025, 3:08:20 PM
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i+=1
        return len(nums)