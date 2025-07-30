# Last updated: 7/29/2025, 9:44:00 PM
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        for i in range(0,len(nums)):
            if nums[i]<0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        c=[]
        while a and b:
            d=b.pop(0)
            c.append(d)
            e=a.pop(0)
            c.append(e)
        return c