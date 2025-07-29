# Last updated: 7/29/2025, 1:32:07 AM
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return
        
        k = k % len(nums)  # Important fix

        a = nums[-k:]
        del nums[-k:]
        for i in range(0,len(nums)):
            a.append(nums[i])
        nums[:]=a

        