# Last updated: 7/14/2025, 3:19:39 PM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        count=len(nums)/3
        a=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for key,value in d.items():
            if value>count:
                a.append(key)
        return a

        