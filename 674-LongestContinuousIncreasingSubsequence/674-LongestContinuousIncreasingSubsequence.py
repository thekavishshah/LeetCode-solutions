# Last updated: 8/7/2025, 3:00:00 AM
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current=1
        longest=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current+=1
                if current>longest:
                    longest=current
            else:
                current=1
        return longest

        