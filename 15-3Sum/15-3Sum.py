# Last updated: 8/5/2025, 3:07:38 AM
class Solution(object):
    def threeSum(self, nums):
        a=[]
        nums.sort()
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1

            while left<right:

                total = nums[i] + nums[left] + nums[right]

                if total==0:
                    a.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    left+=1
        return a


        