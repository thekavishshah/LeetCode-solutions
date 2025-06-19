# Last updated: 6/19/2025, 3:17:46 AM
class Solution(object):
    def sortArrayByParity(self, nums):
        a=[]
        b=[]
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        a.extend(b)
        return a