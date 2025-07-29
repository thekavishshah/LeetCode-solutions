# Last updated: 7/29/2025, 1:56:14 AM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max_count=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
                max_count = max(max_count, count)
            if nums[i]==0:
                count=0
        return max_count




