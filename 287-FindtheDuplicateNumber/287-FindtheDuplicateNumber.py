# Last updated: 7/25/2025, 5:10:55 PM
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for key,value in d.items():
            if value>1:
                return key
        