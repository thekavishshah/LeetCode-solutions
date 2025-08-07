# Last updated: 8/6/2025, 5:49:48 PM
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                count+=1
        return count

        