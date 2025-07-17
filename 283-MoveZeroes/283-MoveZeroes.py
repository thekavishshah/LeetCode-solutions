# Last updated: 7/17/2025, 2:02:24 PM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        a=len(nums)
        while i<a:
            if nums[i]==0:
                b=nums.pop(i)
                nums.append(0)
                a-=1
            else:
                i+=1