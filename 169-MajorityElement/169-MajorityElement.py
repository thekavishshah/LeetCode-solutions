# Last updated: 7/13/2025, 5:50:59 PM
class Solution(object):
    def majorityElement(self, nums):
        d={}
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        count=len(nums)/2
        for key,value in d.items():
            if value>count:
                return key

