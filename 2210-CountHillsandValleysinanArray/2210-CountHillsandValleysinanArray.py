# Last updated: 7/26/2025, 11:37:55 PM
class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i-1]:
                continue
            left=i-1
            while left>=0 and nums[i]==nums[left]:
                left-=1
            right=i+1
            while right < len(nums) and nums[i]==nums[right]:
                right+=1
            if left >= 0 and right < len(nums):
                if nums[i]>nums[left] and nums[i]>nums[right]:
                    count+=1
                if nums[i]<nums[left] and nums[i]<nums[right]:
                    count+=1
        return count
