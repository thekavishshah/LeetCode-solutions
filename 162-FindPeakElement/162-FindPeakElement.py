# Last updated: 7/15/2025, 11:03:15 PM
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        return nums.index(a)
        