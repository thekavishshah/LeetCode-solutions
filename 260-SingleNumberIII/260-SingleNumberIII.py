# Last updated: 7/25/2025, 2:39:58 AM
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        a=[]
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for key,value in d.items():
            if value==1:
                a.append(key)
        return a

        