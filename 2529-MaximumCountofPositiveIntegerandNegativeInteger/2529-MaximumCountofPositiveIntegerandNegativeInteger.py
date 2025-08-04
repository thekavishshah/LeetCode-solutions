# Last updated: 8/4/2025, 12:37:04 AM
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive=0
        negative=0
        for i in range(0,len(nums)):
            if nums[i]>0:
                positive+=1
            if nums[i]<0:
                negative+=1
        return max(positive,negative)