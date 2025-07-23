# Last updated: 7/23/2025, 3:58:56 PM
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=set(nums)
        for i in range(1,len(nums)+1):
            if i not in b:
                a.append(i)
        return a


        