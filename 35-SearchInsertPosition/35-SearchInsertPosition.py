# Last updated: 6/8/2025, 12:21:26 AM
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(0, len(nums)):
            if nums[i]==target:
                return i
            nums.append(target)
            nums.sort()
            for j in range(0,len(nums)):
                if nums[j]==target:
                    return j
        