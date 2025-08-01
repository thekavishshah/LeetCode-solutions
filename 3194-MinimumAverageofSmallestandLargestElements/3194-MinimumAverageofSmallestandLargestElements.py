# Last updated: 8/1/2025, 1:25:25 AM
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        min_avg=float('inf')

        while nums:
            nums.sort()
            a=nums[0]
            b=nums[-1]
            nums.pop(0)
            nums.pop(-1)
            avg=(a+b)/2.0

            if avg<min_avg:
                min_avg=avg
        return min_avg


