# Last updated: 6/15/2025, 11:47:44 PM
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff=-1
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    diff=max(diff,nums[j]-nums[i])
        return diff

                    
                    
        