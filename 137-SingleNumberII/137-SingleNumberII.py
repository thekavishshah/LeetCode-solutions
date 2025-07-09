# Last updated: 7/9/2025, 4:41:37 PM
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for key,value in d.items():
            if value==1:
                return key
        