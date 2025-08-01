# Last updated: 8/1/2025, 1:47:52 AM
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for key,value in d.items():
            if value==1:
                return key
        