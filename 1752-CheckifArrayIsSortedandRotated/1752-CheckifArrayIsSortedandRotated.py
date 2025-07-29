# Last updated: 7/29/2025, 1:23:53 AM
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = min(nums)
        n = len(nums)

        for i in range(n):
            if nums[i] == a:
                c = nums[i:] + nums[:i]
                if c == sorted(c):
                    return True
        return False


        